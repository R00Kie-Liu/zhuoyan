<p align="center">
  <img src="assets/zhuoyan-logo.png" width="144" alt="琢言 Zhuoyan Logo">
</p>
<h1 align="center">琢言 · Zhuoyan</h1>
<p align="center"><strong>让表达自然，让论证准确。</strong></p>
<p align="center">
  <a href="#快速安装">快速安装</a> ·
  <a href="#使用方式">使用方式</a> ·
  <a href="#改写示例">改写示例</a> ·
  <a href="https://github.com/R00Kie-Liu/zhuoyan/releases/tag/v0.1.0">下载 v0.1.0</a>
</p>

琢言是面向中文技术博客、论文和专业解释的写作 skill。它按文本体裁和改写范围审阅内容，清理空泛修辞、翻译腔、讲解评价、编排提示及重复辩解，同时保留事实、证据强度、公式、代码和引用。

## 能做什么

| 模式 | 适合的情况 | 输出 |
| --- | --- | --- |
| 审稿 | 先定位问题，暂不改文 | 位置、问题、原因和修改建议 |
| 轻改 | 结构已经确定，只需润色 | 保留段落顺序，修改局部表达 |
| 深改 | 需要重排结构与论证 | 调整章节、段落和论据顺序，保留事实与立场 |
| 起草 | 已有材料或提纲 | 根据材料成稿，缺失信息保留缺口 |

完整草稿未指定改写程度时，默认轻改。博客侧重问题与推导，论文侧重主张与证据，专业说明侧重动作、条件和依据。

## 快速安装

### Codex 插件

在支持插件命令的 Codex 中运行：

```sh
codex plugin marketplace add R00Kie-Liu/zhuoyan --ref v0.1.0
codex plugin add zhuoyan@r00kie-liu-writing
```

重新打开会话后，显式调用 `$zhuoyan`。支持 repo marketplace 的桌面客户端也可从该安装来源选择插件。安装命令固定到 `v0.1.0`，便于复现。

### 直接安装 skill

下载下表中的独立 skill 包，解压后将整个 `zhuoyan` 文件夹放到项目的 `.agents/skills/`。已有同名目录时先备份旧版。

```text
your-project/
└── .agents/
    └── skills/
        └── zhuoyan/
            ├── SKILL.md
            ├── agents/
            ├── references/
            └── scripts/
```

也可克隆本仓库，复制其中的 `skills/zhuoyan`。其他支持 `SKILL.md` 的工具可按各自约定安装同一文件夹。

### 下载安装包

| 文件 | 用途 |
| --- | --- |
| [zhuoyan-v0.1.0.zip](https://raw.githubusercontent.com/R00Kie-Liu/zhuoyan/5bb547b1600c2e9d1cca6499a646cceb52c5a894/dist/v0.1.0/zhuoyan-v0.1.0.zip) | 独立 skill，解压后直接复制安装 |
| [zhuoyan-plugin-v0.1.0.zip](https://raw.githubusercontent.com/R00Kie-Liu/zhuoyan/5bb547b1600c2e9d1cca6499a646cceb52c5a894/dist/v0.1.0/zhuoyan-plugin-v0.1.0.zip) | 完整插件，含插件清单与 marketplace |
| [SHA256SUMS.txt](https://raw.githubusercontent.com/R00Kie-Liu/zhuoyan/5bb547b1600c2e9d1cca6499a646cceb52c5a894/dist/v0.1.0/SHA256SUMS.txt) | 两个安装包的 SHA-256 校验值 |

下载两个 ZIP 和校验文件至同一目录后，可在支持该命令的系统中校验：

```sh
sha256sum -c SHA256SUMS.txt
```

同样的下载链接也列在 [Release 正文](https://github.com/R00Kie-Liu/zhuoyan/releases/tag/v0.1.0)中。

## 使用方式

只审稿，不改正文：

```text
用 $zhuoyan 审阅这篇文章，按位置、问题、原因和建议给出反馈，不修改正文。
```

轻改，保留结构：

```text
用 $zhuoyan 轻改这篇技术博客，删除空泛修辞和编排提示，保留段落顺序、公式、代码、引用和结论强度。
```

重排论证：

```text
用 $zhuoyan 深改这篇稿件，围绕实际技术问题重排结构，保留关键机制、实验条件、负面结果和适用边界。
```

根据素材起草：

```text
用 $zhuoyan 根据这些实验记录起草技术博客。先提出问题，再解释机制和实验；缺少的数据与来源列为待补信息。
```

## 改写示例

| 原句 | 改写 |
| --- | --- |
| linear attention 是最容易讲糊的一条线。 | linear attention 用固定形状的递推状态承接历史，区别于逐 token 增长的 KV cache。 |
| 多轮 agent 把输入成本推到了更显眼的位置。 | 多轮 agent 会反复处理新增输入，因此需要评估 prefill 的累计开销。 |
| 本节最值得展开的是擦除几何。 | 擦除算子改变旧状态的方式，会影响信息保留。 |

改法取决于原文含义和上下文证据。“更加重要”与“开始受到关注”不能机械互换；“把 KV tile 从 HBM 搬到 SRAM”描述实际数据移动，应保留。

同样需要保护的内容包括：

- 人名、模型名、版本、数值、单位和比较关系。
- 公式、变量、代码、命令、链接和引用。
- 因果方向、结论强弱、适用条件与负面结果。

## 离线审稿脚本

脚本只需 Python 3 标准库，不需要 API key，不发送网络请求。从安装了 skill 的项目根目录执行：

```sh
SKILL_DIR="$PWD/.agents/skills/zhuoyan"
python3 "$SKILL_DIR/scripts/audit_zh_blog.py" path/to/article.md
python3 "$SKILL_DIR/scripts/audit_zh_blog.py" path/to/article.md --json
```

通过标准输入检查：

```sh
python3 "$SKILL_DIR/scripts/audit_zh_blog.py" - < path/to/article.md
```

脚本返回规则、命中位置和建议，忽略 frontmatter、代码、公式、HTML 标签属性和 URL。命中是人工复核线索，不是 AI 检测概率，也不能替代事实核验。正常运行即使命中规则也返回退出码 0，不宜只凭退出码作为文风质量门禁。

在仓库根目录运行回归测试：

```sh
python3 -m unittest discover -s tests -v
```

## 规则与目录

| 文件 | 内容 |
| --- | --- |
| [SKILL.md](skills/zhuoyan/SKILL.md) | 场景判断、任务模式、编辑流程与保护清单 |
| [中文表达参照](skills/zhuoyan/references/ai-tells-zh.md) | 套话、翻译腔、编排提示和空间比喻的语境判断 |
| [推导型博客参照](skills/zhuoyan/references/reasoning-blog-style.md) | 问题、假设、推导、实验与边界的组织方法 |
| [反防御表达](skills/zhuoyan/references/anti-defensive-writing.md) | 区分必要范围与重复辩解 |
| [学术论证](skills/zhuoyan/references/academic-writing.md) | 贡献、实验职责和证据组织 |
| [审稿脚本](skills/zhuoyan/scripts/audit_zh_blog.py) | 离线启发式检查 |
| [回归测试](tests/test_audit.py) | 规则命中、技术反例、保护格式与 CLI 检查 |

根目录的 [plugin.json](plugin.json) 与 [marketplace.json](.agents/plugins/marketplace.json) 提供插件安装信息。GitHub 托管和 Release 可供直接分发；进入 ChatGPT/Codex 官方插件目录需按 [官方发布流程](https://developers.openai.com/codex/plugins/build)单独提交和审核。

## 来源与许可

自有部分沿用 [来源仓库](https://github.com/R00Kie-Liu/R00Kie-Liu.github.io) 的 CC0 1.0，全文见 [LICENSE](LICENSE)。Kiterlin 和 Adkid-Zephyr 的改编部分保留各自 MIT 版权与许可通知，见 [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md)。

规则来源见 [sources.md](skills/zhuoyan/references/sources.md)，更新记录见 [CHANGELOG.md](CHANGELOG.md)。
