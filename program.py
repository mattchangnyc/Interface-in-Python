from interface import PdfParser, EmlParser, FormalParserInterface

pdf_parser = PdfParser()
print(issubclass(PdfParser, FormalParserInterface))
eml_parser = EmlParser()