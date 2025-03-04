import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

# Output directory
OUTPUT_DIR = "./output"
CATEGORIES = ["AC", "HP"]  # Categories for folders

def generate_sample_charts():
    for category in CATEGORIES:
        category_dir = os.path.join(OUTPUT_DIR, category)
        os.makedirs(category_dir, exist_ok=True)  # Ensure directory exists

        # Create a PDF for charts
        pdf_path = os.path.join(category_dir, "outliers.pdf")
        with PdfPages(pdf_path) as pdf:
            for i in range(3):  # Generate 3 sample charts
                fig, ax = plt.subplots()
                x = np.linspace(0, 10, 100)
                y = np.sin(x + i)
                ax.plot(x, y, label=f"Chart {i+1}")
                ax.set_title(f"Outliers Analysis {i+1}")
                ax.legend()
                pdf.savefig(fig)  # Save figure to PDF
                plt.close(fig)  # Close figure to free memory
        
        print(f"Charts saved in {pdf_path}")

if __name__ == "__main__":
    generate_sample_charts()
