import random
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def generate_random_bar_chart(output_file: str = "random_bar_chart.png", count: int = 6) -> Path:
    labels = [f"Item {i + 1}" for i in range(count)]
    values = [random.randint(1, 100) for _ in range(count)]

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


if __name__ == "__main__":
    saved_path = generate_random_bar_chart()
    print(f"柱状图已生成: {saved_path}")
