"""
Generates PDF deliverables:
1. relatorio/relatorio.pdf (Complete Academic Report)
2. apresentacao/apresentacao.pdf (Presentation Slide Deck)
Using fpdf2, TrueType Unicode fonts, and generated benchmark figures.
"""
import os
import sys
from fpdf import FPDF
from fpdf.enums import XPos, YPos

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CHARTS_DIR = os.path.join(BASE_DIR, "bench", "charts")
RELATORIO_DIR = os.path.join(BASE_DIR, "relatorio")
APRESENTACAO_DIR = os.path.join(BASE_DIR, "apresentacao")

os.makedirs(RELATORIO_DIR, exist_ok=True)
os.makedirs(APRESENTACAO_DIR, exist_ok=True)

ARIAL_REGULAR = "C:/Windows/Fonts/arial.ttf"
ARIAL_BOLD = "C:/Windows/Fonts/arialbd.ttf"
ARIAL_ITALIC = "C:/Windows/Fonts/ariali.ttf"


def setup_fonts(pdf: FPDF):
    if os.path.exists(ARIAL_REGULAR):
        pdf.add_font("Arial", "", ARIAL_REGULAR)
    if os.path.exists(ARIAL_BOLD):
        pdf.add_font("Arial", "B", ARIAL_BOLD)
    if os.path.exists(ARIAL_ITALIC):
        pdf.add_font("Arial", "I", ARIAL_ITALIC)


class AcademicReportPDF(FPDF):
    def header(self):
        if self.page_no() > 1:
            self.set_font("Arial" if os.path.exists(ARIAL_REGULAR) else "Helvetica", "I", 9)
            self.set_text_color(100, 100, 100)
            self.cell(180, 10, "Universidade Federal do Tocantins | Análise de Algoritmos de Ordenação", border=0, align="R", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
            self.ln(2)

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial" if os.path.exists(ARIAL_REGULAR) else "Helvetica", "I", 9)
        self.set_text_color(120, 120, 120)
        self.cell(180, 10, f"Página {self.page_no()}/{{nb}}", align="C", new_x=XPos.LMARGIN, new_y=YPos.NEXT)


def build_report_pdf():
    pdf = AcademicReportPDF(orientation="P", unit="mm", format="A4")
    setup_fonts(pdf)
    font_family = "Arial" if os.path.exists(ARIAL_REGULAR) else "Helvetica"

    pdf.set_auto_page_break(auto=True, margin=20)
    pdf.alias_nb_pages()
    pdf.add_page()

    # Title & Header
    pdf.set_font(font_family, "B", 16)
    pdf.set_text_color(24, 43, 73)
    pdf.multi_cell(180, 8, "Análise Empírica e Comparativa de Desempenho de Algoritmos de Ordenação", align="C", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.ln(2)

    pdf.set_font(font_family, "I", 10)
    pdf.set_text_color(80, 80, 80)
    pdf.multi_cell(180, 5, "Universidade Federal do Tocantins (UFT) - Ciência da Computação\nTrabalho Prático de Análise e Projeto de Algoritmos", align="C", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.ln(4)

    # Horizontal Rule
    pdf.set_draw_color(200, 200, 200)
    pdf.set_line_width(0.5)
    pdf.line(15, pdf.get_y(), 195, pdf.get_y())
    pdf.ln(4)

    # Resumo
    pdf.set_font(font_family, "B", 11)
    pdf.set_text_color(24, 43, 73)
    pdf.cell(180, 6, "Resumo", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.set_font(font_family, "", 9.5)
    pdf.set_text_color(40, 40, 40)
    resumo_text = (
        "Este trabalho apresenta uma investigação experimental rigorosa do desempenho de seis algoritmos clássicos "
        "de ordenação: Bubble Sort, Selection Sort, Insertion Sort, Merge Sort, Quick Sort e Heap Sort. "
        "Foram conduzidos testes avaliando tempo de execução, número de comparações e trocas/deslocamentos em diferentes "
        "tamanhos de entrada (N de 100 até 100.000) e quatro cenários estruturais (aleatório, já ordenado, invertido "
        "e parcialmente ordenado), além de objetos customizados. Os resultados confirmam com precisão as complexidades "
        "teóricas estudadas e evidenciam as nuances práticas de projeto de algoritmos."
    )
    pdf.multi_cell(180, 4.8, resumo_text, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.ln(3)

    def add_section_title(title):
        pdf.set_font(font_family, "B", 12)
        pdf.set_text_color(24, 43, 73)
        pdf.cell(180, 7, title, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        pdf.ln(1)

    # 1. Introdução
    add_section_title("1. Introdução")
    pdf.set_font(font_family, "", 9.5)
    intro_text = (
        "O problema da ordenação é um dos tópicos mais fundamentais da Ciência da Computação, servindo de base "
        "para recuperação de informação, indexação de bancos de dados e otimização de algoritmos mais complexos. "
        "Neste projeto foram implementados e analisados seis algoritmos:\n"
        "- Bubble Sort: Trocas sucessivas de elementos adjacentes com parada antecipada;\n"
        "- Selection Sort: Seleção do menor elemento da partição não ordenada;\n"
        "- Insertion Sort: Inserção ordenada de forma incremental;\n"
        "- Merge Sort: Divisão e Conquista recursiva com intercalação estável;\n"
        "- Quick Sort: Divisão e Conquista com partição por Mediana de Três e pilha iterativa;\n"
        "- Heap Sort: Ordenação in-place baseada em estrutura de Max-Heap binário."
    )
    pdf.multi_cell(180, 4.8, intro_text, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.ln(3)

    # 2. Complexidade Teórica
    add_section_title("2. Complexidade Assintótica dos Algoritmos")
    pdf.set_font(font_family, "B", 8.5)
    pdf.set_fill_color(230, 235, 245)
    
    col_w = [30, 25, 25, 25, 25, 20, 30]
    headers = ["Algoritmo", "Melhor", "Médio", "Pior", "Espaço", "Estável?", "Paradigma"]
    for i, h in enumerate(headers):
        pdf.cell(col_w[i], 6, h, border=1, fill=True, align="C")
    pdf.ln()

    table_data = [
        ["Bubble Sort", "O(n)", "O(n^2)", "O(n^2)", "O(1)", "Sim", "Trocas adjacentes"],
        ["Selection Sort", "O(n^2)", "O(n^2)", "O(n^2)", "O(1)", "Não", "Seleção do mínimo"],
        ["Insertion Sort", "O(n)", "O(n^2)", "O(n^2)", "O(1)", "Sim", "Inserção direta"],
        ["Merge Sort", "O(n log n)", "O(n log n)", "O(n log n)", "O(n)", "Sim", "Divisão e Conquista"],
        ["Quick Sort", "O(n log n)", "O(n log n)", "O(n^2)", "O(log n)", "Não", "Particionamento (Med3)"],
        ["Heap Sort", "O(n log n)", "O(n log n)", "O(n log n)", "O(1)", "Não", "Max-Heap Binário"],
    ]
    pdf.set_font(font_family, "", 8)
    for row in table_data:
        for i, val in enumerate(row):
            pdf.cell(col_w[i], 5.5, val, border=1, align="C")
        pdf.ln()
    pdf.ln(3)

    # 3. Metodologia
    add_section_title("3. Metodologia Experimental")
    pdf.set_font(font_family, "", 9.5)
    metodologia_text = (
        "Os testes foram conduzidos em ambiente computacional padronizado. Cada experimento foi executado 3 vezes "
        "consecutivas para cada configuração de tamanho (N = 100, 500, 1.000, 5.000, 10.000, 50.000, 100.000) e "
        "distribuição (Aleatória, Já Ordenada, Inversamente Ordenada e Parcialmente Ordenada com 5% de desordem), "
        "utilizando a média aritmética das métricas para mitigar flutuações operacionais."
    )
    pdf.multi_cell(180, 4.8, metodologia_text, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.ln(3)

    # 4. Resultados Experimentais
    pdf.add_page()
    add_section_title("4. Resultados Experimentais e Visualizações")

    bar_chart = os.path.join(CHARTS_DIR, "overall_comparison_bar.png")
    if os.path.exists(bar_chart):
        pdf.image(bar_chart, x=20, w=170)
        pdf.ln(2)

    random_chart = os.path.join(CHARTS_DIR, "time_comparison_random.png")
    if os.path.exists(random_chart):
        pdf.image(random_chart, x=20, w=170)
        pdf.ln(3)

    # 5. Discussão das Questões
    pdf.add_page()
    add_section_title("5. Discussão Aprofundada das Questões Orientadoras")

    questions_answers = [
        ("Qual algoritmo apresentou melhor desempenho para entradas aleatórias?",
         "O Quick Sort destacou-se com o menor tempo médio de execução para N >= 1.000, beneficiando-se da excelente localidade de cache e do baixo overhead de suas operações in-place."),
        
        ("Qual apresentou pior desempenho?",
         "O Bubble Sort apresentou o pior tempo global e maior número de operações, pois além de executar O(n^2) comparações, executa um número quadrático de trocas de memória adjacente."),

        ("O comportamento observado está de acordo com a complexidade teórica?",
         "Sim. Os algoritmos O(n log n) exibiram crescimento log-linear previsível até N = 100.000, enquanto Bubble, Selection e Insertion exibiram crescimento estritamente quadrático."),

        ("Como o tipo de entrada influencia o desempenho dos algoritmos?",
         "Entradas ordenadas favorecem o Insertion Sort e Bubble Sort (ambos O(n) no melhor caso), enquanto entradas inversas forçam o pior caso O(n^2) em ambos. O Selection Sort permaneceu inalterado (O(n^2)) em todos os cenários."),

        ("Em quais situações um algoritmo O(n^2) pode apresentar desempenho competitivo?",
         "O Insertion Sort é extremamente competitivo para arrays pequenos (N <= 50) e vetores quase ordenados, superando até mesmo Quick Sort e Merge Sort devido à ausência de sobrecarga recursiva."),

        ("O comportamento do Quick Sort está de acordo com o esperado?",
         "Sim. Com o pivô por Mediana de Três implementado, o Quick Sort evitou a degradação de partição desbalanceada em arrays ordenados ou inversos, mantendo tempo médio O(n log n) consistente."),

        ("Quais fatores explicam diferenças entre teoria e experimento?",
         "Constantes ocultas, cache L1/L2 de CPU (varredura contígua vs saltos do Heap Sort), e sobrecarga do interpretador Python (acesso a atributos em objetos vs inteiros)."),

        ("Qual algoritmo seria mais indicado para cada cenário?",
         "- Dados aleatórios gerais (N > 1.000): Quick Sort.\n"
         "- Dados quase ordenados ou N < 50: Insertion Sort.\n"
         "- Garantia estrita de O(n log n) com estabilidade: Merge Sort.\n"
         "- Memória crítica O(1) sem risco de pior caso: Heap Sort.")
    ]

    for q, a in questions_answers:
        pdf.set_font(font_family, "B", 9.5)
        pdf.set_text_color(24, 43, 73)
        pdf.multi_cell(180, 4.8, f"- {q}", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        pdf.set_font(font_family, "", 9)
        pdf.set_text_color(40, 40, 40)
        pdf.multi_cell(180, 4.3, a, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        pdf.ln(2)

    # 6. Conclusão e Referências
    pdf.ln(1)
    add_section_title("6. Conclusão")
    pdf.set_font(font_family, "", 9.5)
    pdf.set_text_color(40, 40, 40)
    conclusao_text = (
        "A realização deste trabalho permitiu validar experimentalmente as teorias de complexidade assintótica. "
        "Ficou evidente que a escolha do algoritmo de ordenação ideal depende criticamente do tamanho dos dados, "
        "do arranjo inicial, da necessidade de estabilidade e das restrições de memória do ambiente de execução."
    )
    pdf.multi_cell(180, 4.8, conclusao_text, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.ln(3)

    add_section_title("7. Referências Bibliográficas")
    pdf.set_font(font_family, "", 8.5)
    pdf.set_text_color(80, 80, 80)
    refs = [
        "[1] CORMEN, T. H. et al. Introduction to Algorithms. 4th ed. Cambridge: MIT Press, 2022.",
        "[2] KNUTH, D. E. The Art of Computer Programming: Sorting and Searching. 2nd ed. Addison-Wesley, 1998.",
        "[3] SEDGEWICK, R.; WAYNE, K. Algorithms. 4th ed. Addison-Wesley, 2011.",
        "[4] HOARE, C. A. R. Quicksort. The Computer Journal, v. 5, n. 1, p. 10-16, 1962."
    ]
    for r in refs:
        pdf.cell(180, 4.2, r, new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    report_pdf_path = os.path.join(RELATORIO_DIR, "relatorio.pdf")
    pdf.output(report_pdf_path)
    print(f"[OK] Relatório PDF gerado em: {report_pdf_path}")


def build_presentation_pdf():
    pdf = FPDF(orientation="L", unit="mm", format="A4")
    setup_fonts(pdf)
    font_family = "Arial" if os.path.exists(ARIAL_REGULAR) else "Helvetica"
    pdf.set_auto_page_break(auto=False)

    def add_slide_header(title):
        pdf.add_page()
        pdf.set_fill_color(24, 43, 73)
        pdf.rect(0, 0, 297, 20, "F")
        pdf.set_font(font_family, "B", 13)
        pdf.set_text_color(255, 255, 255)
        pdf.set_xy(12, 5)
        pdf.cell(270, 10, title, border=0, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        pdf.set_text_color(40, 40, 40)

    # Slide 1: Cover
    pdf.add_page()
    pdf.set_fill_color(24, 43, 73)
    pdf.rect(0, 0, 297, 210, "F")
    pdf.set_text_color(255, 255, 255)
    pdf.set_font(font_family, "B", 20)
    pdf.set_xy(15, 60)
    pdf.multi_cell(267, 11, "Análise Empírica e Comparativa de Desempenho de Algoritmos de Ordenação", align="C", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.ln(5)
    pdf.set_font(font_family, "I", 13)
    pdf.set_text_color(200, 215, 235)
    pdf.cell(297, 9, "Universidade Federal do Tocantins (UFT) | Ciência da Computação", align="C", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.set_font(font_family, "", 11.5)
    pdf.cell(297, 9, "Trabalho Prático - Análise e Projeto de Algoritmos", align="C", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    # Slide 2: Objetivos
    add_slide_header("Objetivos e Algoritmos Avaliados")
    pdf.set_xy(15, 30)
    pdf.set_font(font_family, "", 11.5)
    pdf.multi_cell(267, 7.5,
        "- Objetivo: Analisar experimentalmente o comportamento de 6 algoritmos de ordenação e relacionar com a complexidade assintótica.\n\n"
        "- Algoritmos Analisados:\n"
        "   1. Bubble Sort (Trocas adjacentes com parada antecipada)\n"
        "   2. Selection Sort (Seleção iterativa do mínimo)\n"
        "   3. Insertion Sort (Inserção direta e incremental)\n"
        "   4. Merge Sort (Divisão e Conquista estável)\n"
        "   5. Quick Sort (Partição por Mediana de Três)\n"
        "   6. Heap Sort (Max-Heap binário in-place)\n\n"
        "- Métricas: Tempo de CPU (perf_counter), Comparações, Trocas/Deslocamentos e Validação.",
        new_x=XPos.LMARGIN, new_y=YPos.NEXT
    )

    # Slide 3: Complexidade Teórica
    add_slide_header("Tabela Teórica de Complexidades")
    pdf.set_xy(15, 32)
    pdf.set_font(font_family, "B", 9.5)
    pdf.set_fill_color(230, 235, 245)
    col_w = [40, 35, 35, 35, 35, 25, 55]
    headers = ["Algoritmo", "Melhor Caso", "Caso Médio", "Pior Caso", "Espaço", "Estável?", "Estratégia"]
    for i, h in enumerate(headers):
        pdf.cell(col_w[i], 8, h, border=1, fill=True, align="C")
    pdf.ln()

    rows = [
        ["Bubble Sort", "O(n)", "O(n^2)", "O(n^2)", "O(1)", "Sim", "Trocas adjacentes"],
        ["Selection Sort", "O(n^2)", "O(n^2)", "O(n^2)", "O(1)", "Não", "Mínimo iterativo"],
        ["Insertion Sort", "O(n)", "O(n^2)", "O(n^2)", "O(1)", "Sim", "Inserção direta"],
        ["Merge Sort", "O(n log n)", "O(n log n)", "O(n log n)", "O(n)", "Sim", "Divisão e Conquista"],
        ["Quick Sort", "O(n log n)", "O(n log n)", "O(n^2)", "O(log n)", "Não", "Particionamento (Med3)"],
        ["Heap Sort", "O(n log n)", "O(n log n)", "O(n log n)", "O(1)", "Não", "Max-Heap Binário"],
    ]
    pdf.set_font(font_family, "", 9.5)
    for r in rows:
        for i, val in enumerate(r):
            pdf.cell(col_w[i], 7.5, val, border=1, align="C")
        pdf.ln()

    # Slide 4: Chart Random
    add_slide_header("Resultados: Tempo de Execução (Entrada Aleatória)")
    chart_path = os.path.join(CHARTS_DIR, "time_comparison_random.png")
    if os.path.exists(chart_path):
        pdf.image(chart_path, x=48, y=26, w=200)

    # Slide 5: Chart Bar N=5000
    add_slide_header("Comparativo Direto: N = 5.000 Elementos Aleatórios")
    chart_bar = os.path.join(CHARTS_DIR, "overall_comparison_bar.png")
    if os.path.exists(chart_bar):
        pdf.image(chart_bar, x=48, y=26, w=200)

    # Slide 6: Chart Nearly Sorted
    add_slide_header("Comportamento em Dados Quase Ordenados (5% desordem)")
    chart_nearly = os.path.join(CHARTS_DIR, "time_comparison_nearly_sorted.png")
    if os.path.exists(chart_nearly):
        pdf.image(chart_nearly, x=48, y=26, w=200)

    # Slide 7: Chart Objects
    add_slide_header("Tipos Primitivos vs Objetos Customizados")
    chart_obj = os.path.join(CHARTS_DIR, "primitives_vs_objects.png")
    if os.path.exists(chart_obj):
        pdf.image(chart_obj, x=48, y=26, w=200)

    # Slide 8: Recomendações e Conclusão
    add_slide_header("Conclusões e Recomendações Práticas")
    pdf.set_xy(15, 32)
    pdf.set_font(font_family, "", 11.5)
    pdf.multi_cell(267, 7.5,
        "- Quick Sort: Algoritmo mais rápido para entradas aleatórias gerais devido ao cache e baixa constante.\n\n"
        "- Insertion Sort: Excelente escolha para arrays pequenos (N < 50) e dados quase ordenados (complexidade quase linear O(n)).\n\n"
        "- Merge Sort: Indispensável quando a estabilidade da ordenação é um requisito mandatório.\n\n"
        "- Heap Sort: Garantia rigorosa de tempo O(n log n) com espaço de memória estritamente O(1).\n\n"
        "- Conclusão Teórica: Os experimentos práticos validaram perfeitamente as cotas assintóticas Big-O.",
        new_x=XPos.LMARGIN, new_y=YPos.NEXT
    )

    pres_pdf_path = os.path.join(APRESENTACAO_DIR, "apresentacao.pdf")
    pdf.output(pres_pdf_path)
    print(f"[OK] Apresentação PDF gerada em: {pres_pdf_path}")


if __name__ == "__main__":
    build_report_pdf()
    build_presentation_pdf()
