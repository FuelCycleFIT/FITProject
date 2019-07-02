pdf: FITPaperEx1.pdf 

FITPaperEx1.pdf: FITPaperEx1.tex Part_1.tex Part_2.tex Part_3.tex Part_4.tex acronyms.tex mybibfile.bib
	pdflatex FITPaperEx1.tex


bib:
	pdflatex FITPaperEx1.tex               
	bibtex FITPaperEx1
	pdflatex FITPaperEx1.tex
	pdflatex FITPaperEx1.tex

clean:
	rm -vf *.aux *.log *.blg *.bbl FITPaperEx1.pdf
