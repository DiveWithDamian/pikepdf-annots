"""
pikepdf_annots - PikePDF helper utilities

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
from dataclasses import dataclass
from decimal import Decimal
from typing import Optional, Union, List


@dataclass(repr=True, frozen=True)
class AnnotationMatcher:
    """Name of annotation to match."""

    name: Union[List[Decimal], str]
    human_name: Optional[str] = None

    def __post_init__(self) -> None:
        if self.human_name is None:
            object.__setattr__(self, 'human_name', self.name)

    def matches(self, annotation) -> bool:
        """Compare our instance to the specified annotation."""
        # Text annotation
        if "/T" in annotation:
            return annotation.T == self.name
        # Position annotation
        return annotation.Rect == self.name
