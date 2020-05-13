GNU nano 2.5.3                                              File: README.md                                                                                         Modified  


## TAKEN AND MODIFIED FROM ERIN'S SZ_PINT.

#note: you must update the file called  _bookdown.yml with a list of what to knit into the bookdown.

# These notebooks contain a workflow for {{cookiecutter.project_title}}.

These are collected into an bookdown book.

To render the book:

```sh
module load R/3.5.0 rstudio #or whatever version of R you use & have packages installed in
```

## make sure the current working directory is set to {{cookiecutter.project_folder_name}}/notebooks/Rmd
This part of the script will remove any existing reports and overwrite them with new bookdown.

```sh
rm -rf ../../reports/Rmd_rendered/*
rm {{cookiecutter.project_folder_name}}_bookdown.*
rm 0*.md
```
Then open up rstudio and run this line :)
```{r}
bookdown::render_book('index.Rmd', output_format = "bookdown::gitbook", output_dir = '../../reports/Rmd_rendered')
```
