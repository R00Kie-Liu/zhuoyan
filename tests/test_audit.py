from pathlib import Path
import json
import runpy
import subprocess
import sys
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / 'skills/zhuoyan/scripts/audit_zh_blog.py'
audit = runpy.run_path(str(SCRIPT))['audit']
STYLE_RULES = {'exposition-evaluation', 'editorial-retention-frame', 'salience-spatial-metaphor'}


class AuditTests(unittest.TestCase):
    def rules(self, text):
        return {item['rule'] for item in audit(text, 100)['findings']}

    def test_exposition_evaluation(self):
        for text in ['linear attention 是最容易讲糊的一条线。', 'HISA 是最容易理解的一条。',
                     '这个方法值得单独拿出来讲。', '其中最值得进一步展开的是擦除几何。',
                     'RWKV 的关系尤其值得单独说一下。', '这些观察值得放进这里。',
                     'KDA 适合单独拿出来讲。']:
            with self.subTest(text=text):
                self.assertIn('exposition-evaluation', self.rules(text))

    def test_editorial_framing(self):
        for text in ['这里保留两个判断。', '如果只用一句话收束这篇：a。']:
            with self.subTest(text=text):
                self.assertIn('editorial-retention-frame', self.rules(text))

    def test_salience_metaphors(self):
        for text in ['把输入成本推到更显眼的位置。', '多轮 agent 把输入成本推到了更显眼的位置。',
                     '把 X 放到更加醒目的位置。', '将状态管理推向舞台中央。',
                     '让状态管理站到聚光灯下。', 'selector/indexer 成为新的主战场。']:
            with self.subTest(text=text):
                self.assertIn('salience-spatial-metaphor', self.rules(text))

    def test_technical_and_reading_counterexamples(self):
        for text in ['累计衰减连乘容易下溢。', '语义相近的事实可能在 latent space 中混淆。',
                     '这个 token 值不值得写入由训练目标决定。', '这里保留两个候选块，再选择 top-k。',
                     '状态管理因此变得更加重要。', '状态管理开始受到关注。',
                     '状态管理进入了大家的视野。', '将 KV tile 从 HBM 搬到 SRAM。',
                     '把 KV 推到 GPU 的缓存队列。', '可见范围缩小到最近 W 个位置。',
                     'top-k 地址离散，还可能把执行瓶颈推向访存。', '梯度把参数推向更强写入。',
                     '上下文从 32K 推到 128K。', '用固定窗口截断单层视野。', '这篇资料值得单独读。']:
            with self.subTest(text=text):
                self.assertFalse(self.rules(text) & STYLE_RULES)

    def test_protected_formats(self):
        for text in ['```text\n把输入成本推到更显眼的位置。\n```',
                     '~~~text\n这里保留两个判断\n~~~', '`最容易讲糊`',
                     '$$\\text{把输入成本推到更显眼的位置}$$',
                     '---\ndescription: 最容易讲糊\n---\n',
                     '<a id="2-趋势一selectorindexer-成为新的主战场"></a>']:
            with self.subTest(text=text):
                self.assertFalse(self.rules(text) & STYLE_RULES)

    def test_visible_html_text_is_audited(self):
        self.assertIn('salience-spatial-metaphor', self.rules('<strong>把成本推到更显眼的位置。</strong>'))

    def test_line_numbers_after_masking(self):
        text = '```text\n最容易讲糊\n```\n把成本推到更显眼的位置。\n'
        finding = next(x for x in audit(text, 100)['findings'] if x['rule'] == 'salience-spatial-metaphor')
        self.assertEqual(finding['line'], 4)

    def test_cli_path_with_spaces_and_zero_exit_for_findings(self):
        with tempfile.TemporaryDirectory(prefix='audit input ') as folder:
            path = Path(folder) / 'article sample.md'
            path.write_text('把成本推到更显眼的位置。\n', encoding='utf-8')
            result = subprocess.run([sys.executable, str(SCRIPT), str(path), '--json'],
                                    cwd=folder, text=True, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertTrue(json.loads(result.stdout)['findings'])

    def test_cli_stdin(self):
        result = subprocess.run([sys.executable, str(SCRIPT), '-', '--json'],
                                input='累计衰减连乘容易下溢。\n', text=True, capture_output=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout)['findings'], [])

    def test_cli_rejects_invalid_limit(self):
        result = subprocess.run([sys.executable, str(SCRIPT), '-', '--max-findings', '0'],
                                input='', text=True, capture_output=True)
        self.assertEqual(result.returncode, 2)


if __name__ == '__main__':
    unittest.main()
