from fpdf import FPDF

def read_summary(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        summary_text = f.read()
    return summary_text

class ResumeReport(FPDF):
    def __init__(self, title, subtitle):
        super().__init__()
        self.title = title
        self.subtitle = subtitle

    def header(self):
        # No header for this type of report
        pass

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, 'Page %s' % self.page_no(), 0, 0, 'C')

    def add_cover_page(self, summary):
        # Add a page
        self.add_page()
        # Title
        self.set_font('Arial', 'B', 26)
        self.set_text_color(30, 30, 100)  # Dark Blue
        self.cell(0, 20, self.title, 0, 1, 'C')

        # Subtitle
        self.set_font('Arial', 'I', 16)
        self.set_text_color(80, 80, 80)  # Gray
        self.cell(0, 15, self.subtitle, 0, 1, 'C')

        self.ln(15)

        # Body summary
        self.set_font('Times', '', 14)
        self.set_text_color(0, 0, 0)  # Black
        self.multi_cell(0, 10, summary.strip())

def main():
    input_file = 'C:/Users/pramo/intern/2nd/sample.txt'
    output_pdf = 'C:/Users/pramo/intern/final_report.pdf'

    summary = read_summary(input_file)

    report = ResumeReport('My Resume', 'Front Page Report')
    report.add_cover_page(summary)

    report.output(output_pdf)
    print(f'Report generated: {output_pdf}')

if __name__ == '__main__':
    main()