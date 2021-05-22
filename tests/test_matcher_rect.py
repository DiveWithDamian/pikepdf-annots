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
from decimal import Decimal

from pikepdf_annots import AnnotationMatcher


def test_rect_matcher_success():
    class BasicRectAnnotationObject:
        def __getattr__(self, item):
            if item == "Rect":
                return [Decimal("325.611"), Decimal("459.248"),
                        Decimal("334.32"), Decimal("468.189")]
            return None

        def __contains__(self, item):
            return False

    matcher = AnnotationMatcher([Decimal("325.611"), Decimal("459.248"),
                                 Decimal("334.32"), Decimal("468.189")],
                                "Example Field")
    assert matcher.matches(BasicRectAnnotationObject()) is True


def test_rect_matcher_failure():
    class BasicRectAnnotationObject:
        def __getattr__(self, item):
            if item == "Rect":
                return [Decimal("100.611"), Decimal("825.248"),
                        Decimal("532.32"), Decimal("243.189")]
            return None

        def __contains__(self, item):
            return False

    matcher = AnnotationMatcher([Decimal("325.611"), Decimal("459.248"),
                                 Decimal("334.32"), Decimal("468.189")],
                                "Example Field")
    assert matcher.matches(BasicRectAnnotationObject()) is False
