# polish-technical-blog-zh

中文技术博客、论文和专业解释的审稿与润色 skill。清理空泛修辞、讲解评价、编排提示及重复辩解，保留事实、证据强度、公式、代码和引用。

支持审稿、轻改、深改和起草；完整草稿未指定改写程度时默认轻改。内置 Python 脚本只提供可定位的启发式线索，不计算“AI 概率”。

## 在 Codex 中安装

本仓库提供纯 skill 插件。支持插件命令的 Codex 可添加本仓库的 marketplace，再安装插件：

```sh
codex plugin marketplace add R00Kie-Liu/polish-technical-blog-zh --ref v0.1.0
codex plugin add polish-technical-blog-zh@r00kie-liu-writing
```

重新打开会话后调用 `$polish-technical-blog-zh`。支持 repo marketplace 的桌面客户端也可从该安装来源选择插件。不同客户端的界面和功能可能不同。

## 直接安装 skill 文件夹

从 [Releases](https://github.com/R00Kie-Liu/polish-technical-blog-zh/releases) 下载 `polish-technical-blog-zh-v0.1.0.zip`，解压后把整个 `polish-technical-blog-zh` 文件夹放进项目的 `.agents/skills/`。已有同名目录时先备份旧版。

也可以克隆仓库，将其中的 `skills/polish-technical-blog-zh` 复制到项目的 `.agents/skills/`。包含根目录 `plugin.json` 的完整插件包是另一个独立下载项。

其他支持 `SKILL.md` 的工具可按各自约定安装 skill 文件夹。

## 用法

只审稿，不改正文：

```text
用 $polish-technical-blog-zh 审阅这篇文章，按位置、问题和建议给出反馈，不修改正文。
```

轻改，保留结构：

```text
用 $polish-technical-blog-zh 轻改这篇技术博客，删除空泛修辞和编排提示，保留段落顺序、公式、代码、引用和结论强度。
```

重排论证：

```text
用 $polish-technical-blog-zh 深改这篇稿件，围绕实际技术问题重排结构，保留关键机制、实验条件、负面结果和适用边界。
```

规则按语义判断。“把输入成本推到更显眼的位置”应改成具体的成本或重要性变化；“把 KV tile 从 HBM 搬到 SRAM”描述实际数据移动，应保留。“更加重要”也不能在没有依据时改成“大家开始关注”。

## 机械审稿

安装 skill 后，在项目根目录执行：

```sh
SKILL_DIR="$PWD/.agents/skills/polish-technical-blog-zh"
python3 "$SKILL_DIR/scripts/audit_zh_blog.py" path/to/article.md
python3 "$SKILL_DIR/scripts/audit_zh_blog.py" path/to/article.md --json
```

只需 Python 3 标准库，不需要 API key，不发送网络请求。脚本忽略 frontmatter、代码、公式、HTML 标签属性和 URL，保留正文中的可复核命中。正常执行时，即使命中规则也返回 0；不要只凭退出码把它用作质量门禁。

运行本仓库的回归检查：

```sh
python3 -m unittest discover -s tests -v
```

## 仓库结构

- `plugin.json`：Agent Plugins 入口。
- `.agents/plugins/marketplace.json`：GitHub marketplace 安装来源。
- `skills/polish-technical-blog-zh/SKILL.md`：skill 入口与编辑流程。
- `skills/polish-technical-blog-zh/references/`：文风、论证与来源参照。
- `skills/polish-technical-blog-zh/scripts/audit_zh_blog.py`：离线审稿。
- `tests/`：规则与命令行回归检查。

GitHub 托管与 Release 分发可让他人直接安装。本仓库不代表已经进入 ChatGPT/Codex 官方插件目录；官方目录需要按 [插件发布流程](https://developers.openai.com/codex/plugins/build)单独提交和审核。

## 来源与许可

自有部分沿用 [来源仓库](https://github.com/R00Kie-Liu/R00Kie-Liu.github.io) 的 CC0 1.0，全文见 [LICENSE](LICENSE)。Kiterlin 和 Adkid-Zephyr 的改编部分保留 MIT 版权与许可通知，见 [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md)；再分发这些部分时需保留相应通知。

规则来源见 [sources.md](skills/polish-technical-blog-zh/references/sources.md)，版本记录见 [CHANGELOG.md](CHANGELOG.md)。
