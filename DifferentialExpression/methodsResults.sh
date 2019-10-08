#!/usr/bin/env bash
# methodsResults.sh
R -e "rmarkdown::render('methodsResults.Rmd', output_format='md_document')"
