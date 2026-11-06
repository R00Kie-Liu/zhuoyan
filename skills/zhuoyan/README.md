# 琢言 · Zhuoyan

让表达自然，让论证准确。

面向中文技术博客、论文和专业解释的写作 skill。支持审稿、轻改、深改和起草，保留事实、证据强度、公式、代码、引用和必要条件。

它会根据文本体裁调整编辑重点，清理翻译腔、空泛评价、编排提示和重复辩解。内置 Python 脚本可定位部分常见句式；结果是人工复核线索，不是 AI 检测概率。

## 安装到 Codex 项目

解压发行包，将整个 `zhuoyan` 目录复制到项目的 `.agents/skills/` 下：

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

保留目录名与子目录结构。若已有同名 skill，先备份旧目录，再替换；不要将新版本继续嵌套到旧目录里。重新打开项目会话后，显式使用 `$zhuoyan` 调用。

其他支持 `SKILL.md` 的工具可以按各自的技能目录安装；本发行包在 Codex 环境中验证，未逐一测试其他客户端。

## 用法

审稿，保留原文：

```text
用 $zhuoyan 审阅这篇文章，只给出位置、问题和建议，不修改正文。
```

轻改，保留结构：

```text
用 $zhuoyan 轻改这篇技术博客，删除空泛的讲解评价和编排提示，保留段落顺序、公式、代码、引用和结论强度。
```

重写结构：

```text
用 $zhuoyan 深改这篇稿件，围绕实际技术问题重排论证。保留全部关键机制、实验条件、负面结果和适用边界。
```

未指定改写程度时，完整草稿默认轻改。技能不会为补齐文章而捏造实验、来源或作者经历。

## 机械审稿脚本

脚本仅依赖 Python 3 标准库，不需要 API key，也不发送网络请求。以下命令从项目根目录执行：

```sh
SKILL_DIR="$PWD/.agents/skills/zhuoyan"
python3 "$SKILL_DIR/scripts/audit_zh_blog.py" path/to/article.md
python3 "$SKILL_DIR/scripts/audit_zh_blog.py" path/to/article.md --json
```

也可通过标准输入检查：

```sh
python3 "$SKILL_DIR/scripts/audit_zh_blog.py" - < path/to/article.md
```

脚本忽略 frontmatter、代码、公式、HTML 标签属性和 URL，报告命中位置及修改建议。正常执行时，即使命中规则也返回退出码 0；请读取报告，不要把它直接当成文风质量的 CI 门禁。模型编辑时仍需人工核对事实和技术含义。

例如，本版会提示检查“linear attention 是最容易讲糊的一条线”，但不会因为“累计衰减连乘容易下溢”含有“容易”就要求删除实际风险。

## 目录

- `SKILL.md`：入口、任务模式、编辑流程与保护清单。
- `references/ai-tells-zh.md`：中文表达的语境审稿线索。
- `references/reasoning-blog-style.md`：推导型技术博客的论证方法。
- `references/anti-defensive-writing.md`：区分必要范围与无信息的辩解。
- `references/academic-writing.md`：论文贡献、实验职责与证据组织。
- `scripts/audit_zh_blog.py`：离线启发式审稿。
- `agents/openai.yaml`：支持该元数据的客户端显示配置。

## 来源与许可

本包沿用来源仓库对自有部分的 CC0 1.0 许可，全文见 [LICENSE](LICENSE)。改编自 Kiterlin 与 Adkid-Zephyr 的部分保留各自 MIT 许可和版权声明；这部分的再分发须保留相应通知。不能将整个包概括为没有任何通知要求的 CC0 内容。

来源仓库为 [R00Kie-Liu/R00Kie-Liu.github.io](https://github.com/R00Kie-Liu/R00Kie-Liu.github.io)。具体来源见 [references/sources.md](references/sources.md) 与 [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md)。

版本：`0.1.0`。更新记录见 [CHANGELOG.md](CHANGELOG.md)。
