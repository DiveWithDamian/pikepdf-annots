PikePDF helper utilities
========================

Helper utilities for editing PDFs using [PikePDF](https://github.com/pikepdf/pikepdf).

## Example usage

```python3
from pathlib import PosixPath
from pikepdf_annots import EditableForm, AnnotationMatcher

class ExampleForm(EditableForm):
    def _get_source_pdf(self) -> PosixPath:
        return PosixPath('source.pdf')

with ExampleForm() as pdf:
    pdf.update_annotation(0, AnnotationMatcher("First Name"), "Bob")
    pdf.update_annotation(0, AnnotationMatcher("Last Name"), "Smoth")
```
