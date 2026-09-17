import random
from pathlib import Path


def _print_text_bar_chart(labels, values):
    max_value = max(values)
    scale = 40 / max_value if max_value else 1
    print("Random Bar Chart (Text Mode)")
    for label, value in zip(labels, values):
        bar = "█" * max(1, int(value * scale))
        print(f"{label:>8} | {bar} {value}")


def _save_image_bar_chart(labels, values, output_file):
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    plt.figure(figsize=(8, 5))
    bars = plt.bar(labels, values, color="skyblue", edgecolor="black")
    plt.title("Random Bar Chart")
    plt.xlabel("Category")
    plt.ylabel("Value")
    plt.ylim(0, max(values) + 10)

    for bar, value in zip(bars, values):
        plt.text(bar.get_x() + bar.get_width() / 2, value + 1, str(value), ha="center", va="bottom")

    output_path = Path(output_file).resolve()
    plt.tight_layout()
    plt.savefig(output_path, dpi=150)
    plt.close()
    return output_path


def generate_random_bar_chart(output_file: str = "random_bar_chart.png", count: int = 6):
    labels = [f"Item {i + 1}" for i in range(count)]
    values = [random.randint(1, 100) for _ in range(count)]

    try:
        output_path = _save_image_bar_chart(labels, values, output_file)
        return f"柱状图已生成: {output_path}"
    except ModuleNotFoundError:
        _print_text_bar_chart(labels, values)
        return "未安装 matplotlib，已输出文本柱状图。"


if __name__ == "__main__":
    message = generate_random_bar_chart()
    print(message)
