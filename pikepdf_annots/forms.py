"""
pikepdf_annotations - PikePDF helper utilities

MIT License

Copyright (c) 2021 Damian Zaremba

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
from pathlib import PosixPath
from types import TracebackType
from typing import Set, Dict, Optional, Type, Union

import pikepdf


class EditableForm:
    """Editable form using PikePDF."""
    _pdf = None

    def get_annotations(self) -> Dict[int, Set[str]]:
        """Get all annotation names."""
        annotations = {}
        for n, page in enumerate(self._pdf.pages):
            annotations[n] = set()
            for annotation in page.Annots:
                for flag in {"/T", "/Yes", "/Off", "/Opt",
                             "/0", "/1", "/2", "/3", "/4",
                             "/5", "/6", "/7", "/8", "/9"}:
                    if flag in annotation:
                        name = getattr(annotation, flag.lstrip("/"))
                        annotations[n].add(name)
        return annotations

    def update_annotation(self, page: int,
                          matcher,
                          value: Union[bool, str]) -> None:
        """Update annotations."""
        for annotation in self._pdf.pages[page].Annots:
            if matcher.matches(annotation):
                # Booleans: /Off & /Yes
                # Checkbox: /0, /1, /2, /3, /4 etc
                if value is True:
                    for flag in {"/0", "/1", "/2", "/3", "/4",
                                 "/5", "/6", "/7", "/8", "/9",
                                 "/Yes"}:
                        if flag in annotation.AP.N:
                            annotation.AS = pikepdf.Name(flag)  # pyre-ignore

                elif value is False:
                    annotation.AS = pikepdf.Name("/Off")  # pyre-ignore

                # String
                else:
                    annotation.V = str(value)
                    if "/AP" in annotation:
                        # Embedded font encoded version of text?
                        # Just drop this, the viewers all seem to deal with it
                        # (at least using standard fonts)
                        del annotation["/AP"]

    def _get_source_pdf(self) -> PosixPath:
        """Get the source PDF path as a PosixPath."""
        raise NotImplementedError()

    def __enter__(self) -> "EditableForm":
        """Context constructor."""
        source_file = self._get_source_pdf()
        if not source_file.is_file():
            raise RuntimeError(f"{source_file.as_posix()} does not exist")

        self._pdf = pikepdf.open(source_file)
        return self

    def __exit__(self,
                 exc_type: Optional[Type[BaseException]],
                 exc_val: Optional[BaseException],
                 exc_tb: Optional[TracebackType]) -> bool:
        """Context destructor."""
        return self._pdf.close()

    def export(self, path: PosixPath) -> None:
        """Export edited PDF to disk."""
        self._pdf.save(path.as_posix())
