#!/usr/bin/env bash
R -e "rmarkdown::render('methodsResults.Rmd', output_format='md_document')"
