from fpdf import FPDF

def analyze_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            print(f"File content preview (first 100 chars): {content[:100]}")
            lines = content.splitlines()

        line_count = len(lines)
        word_count = sum(len(line.split()) for line in lines)
        char_count = len(content)

        print(f"Analysis - Lines: {line_count}, Words: {word_count}, Characters: {char_count}")
        return line_count, word_count, char_count
    except Exception as e:
        print(f"Error reading file: {e}")
        return 0, 0, 0

class PDFReport(FPDF):
    def __init__(self, title):
        super().__init__()
        self.title = title

    def header(self):
        self.set_font('Arial', 'B', 16)
        self.cell(0, 10, self.title, 0, 1, 'C')
        self.ln(10)

    def add_analysis(self, line_count, word_count, char_count):
        self.set_font('Arial', '', 12)
        self.cell(0, 10, f'Total Lines: {line_count}', 0, 1)
        self.cell(0, 10, f'Total Words: {word_count}', 0, 1)
        self.cell(0, 10, f'Total Characters: {char_count}', 0, 1)
        self.ln(10)

def main():
    input_file = 'C:/Users/pramo/intern/2nd/sample.txt'
    output_pdf = 'C:/Users/pramo/intern/analysis_report.pdf'

    lines, words, chars = analyze_file(input_file)
    if lines == 0 and words == 0 and chars == 0:
        print("File analysis failed or file empty.")
        return

    report = PDFReport('File Analysis Report')
    report.add_page()
    report.add_analysis(lines, words, chars)
    report.output(output_pdf)

    print(f'Report generated: {output_pdf}')

if __name__ == '__main__':
    main()
