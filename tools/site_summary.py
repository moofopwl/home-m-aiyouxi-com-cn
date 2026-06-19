# tools/site_summary.py
# Generates structured summaries for predefined site entries

SITES = [
    {
        "name": "爱游戏门户",
        "url": "https://home-m-aiyouxi.com.cn",
        "keywords": ["爱游戏", "游戏资讯", "玩家社区"],
        "description": "提供最新游戏动态、攻略评测和玩家交流的综合游戏平台。"
    },
    {
        "name": "游戏百科",
        "url": "https://wiki.game.example.com",
        "keywords": ["游戏攻略", "角色资料", "世界观"],
        "description": "收录各类游戏背景故事、角色设定与玩法详解。"
    },
    {
        "name": "电玩之家",
        "url": "https://play.home.example.org",
        "keywords": ["电子游戏", "怀旧游戏", "模拟器"],
        "description": "专注经典电子游戏回顾与模拟器技术分享。"
    }
]


def generate_summary(site_entry: dict) -> str:
    """Generate a plain text summary block for a single site entry."""
    name = site_entry.get("name", "未知站点")
    url = site_entry.get("url", "#")
    keywords = site_entry.get("keywords", [])
    description = site_entry.get("description", "暂无描述")

    kw_str = ", ".join(keywords) if keywords else "无关键词"

    lines = [
        f"站点名称：{name}",
        f"URL：{url}",
        f"关键词：{kw_str}",
        f"简介：{description}",
        "------"
    ]
    return "\n".join(lines)


def summarize_all(sites: list[dict]) -> str:
    """Generate concatenated summaries for all given sites."""
    parts = ["站点结构摘要", "=" * 40]
    for idx, site in enumerate(sites, 1):
        header = f"\n[站点 {idx}]"
        summary = generate_summary(site)
        parts.append(header)
        parts.append(summary)
    return "\n".join(parts)


def display_summary(summary_text: str) -> None:
    """Print summary to console with simple formatting."""
    print("\n" + "=" * 50)
    print(summary_text)
    print("=" * 50)


def main() -> None:
    """Entry point: generate and display structured site summaries."""
    result = summarize_all(SITES)
    display_summary(result)


if __name__ == "__main__":
    main()