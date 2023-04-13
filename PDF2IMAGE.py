import pypdfium2 as pdfium

def MyPdf2Image(addr, out='.'):
    pdf = pdfium.PdfDocument(addr)
    n_pages = len(pdf)
    for page_number in range(n_pages):
    #     page = pdf.get_page(page_number)
    #     page.render
    #     pil_image = page.render(
    #         scale=1,
    #         rotation=0,
    #         crop=(0, 0, 0, 0)
    #     )

        page_indices = [i for i in range(n_pages)]  # all pages
        renderer = pdf.render(
            pdfium.PdfBitmap.to_pil,
            page_indices = 0,
            scale = 300/72,  # 300dpi resolution
        )
        for i, image in zip(page_indices, renderer):
            image.save("IMG/out_%0*d.jpg" % (page_number, i))


        # pil_image
        # pil_image.save(f"{out}/image_{page_number+1}.png")