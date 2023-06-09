import re
from _typeshed import Incomplete
from typing import Any, ClassVar, NamedTuple
from xml.etree.ElementTree import Element

from markdown.core import Markdown

def build_inlinepatterns(md, **kwargs): ...

NOIMG: str
BACKTICK_RE: str
ESCAPE_RE: str
EMPHASIS_RE: str
STRONG_RE: str
SMART_STRONG_RE: str
SMART_EMPHASIS_RE: str
SMART_STRONG_EM_RE: str
EM_STRONG_RE: str
EM_STRONG2_RE: str
STRONG_EM_RE: str
STRONG_EM2_RE: str
STRONG_EM3_RE: str
LINK_RE: str
IMAGE_LINK_RE: str
REFERENCE_RE: str
IMAGE_REFERENCE_RE: str
NOT_STRONG_RE: str
AUTOLINK_RE: str
AUTOMAIL_RE: str
HTML_RE: str
ENTITY_RE: str
LINE_BREAK_RE: str

def dequote(string): ...

class _EmStrongItemBase(NamedTuple):
    pattern: re.Pattern[str]
    builder: str
    tags: str

class EmStrongItem(_EmStrongItemBase): ...

class Pattern:
    ANCESTOR_EXCLUDES: ClassVar[tuple[Incomplete, ...]]
    pattern: Any
    compiled_re: re.Pattern[str]
    md: Markdown
    def __init__(self, pattern, md: Markdown | None = None) -> None: ...
    def getCompiledRegExp(self): ...
    def handleMatch(self, m: re.Match[str]) -> str | Element | None: ...
    def type(self): ...
    def unescape(self, text): ...

class InlineProcessor(Pattern):
    safe_mode: bool
    def __init__(self, pattern, md: Markdown | None = None) -> None: ...
    def handleMatch(self, m: re.Match[str], data) -> tuple[Element, int, int] | tuple[None, None, None]: ...  # type: ignore[override]

class SimpleTextPattern(Pattern): ...
class SimpleTextInlineProcessor(InlineProcessor): ...
class EscapeInlineProcessor(InlineProcessor): ...

class SimpleTagPattern(Pattern):
    tag: Any
    def __init__(self, pattern, tag) -> None: ...

class SimpleTagInlineProcessor(InlineProcessor):
    tag: Any
    def __init__(self, pattern, tag) -> None: ...

class SubstituteTagPattern(SimpleTagPattern): ...
class SubstituteTagInlineProcessor(SimpleTagInlineProcessor): ...

class BacktickInlineProcessor(InlineProcessor):
    ESCAPED_BSLASH: Any
    tag: str
    def __init__(self, pattern) -> None: ...

class DoubleTagPattern(SimpleTagPattern): ...
class DoubleTagInlineProcessor(SimpleTagInlineProcessor): ...
class HtmlInlineProcessor(InlineProcessor): ...

class AsteriskProcessor(InlineProcessor):
    PATTERNS: ClassVar[list[EmStrongItem]]
    def build_single(self, m, tag, idx): ...
    def build_double(self, m, tags, idx): ...
    def build_double2(self, m, tags, idx): ...
    def parse_sub_patterns(self, data, parent, last, idx) -> None: ...
    def build_element(self, m, builder, tags, index): ...

class UnderscoreProcessor(AsteriskProcessor): ...

class LinkInlineProcessor(InlineProcessor):
    RE_LINK: ClassVar[re.Pattern[str]]
    RE_TITLE_CLEAN: ClassVar[re.Pattern[str]]
    def getLink(self, data, index): ...
    def getText(self, data, index): ...

class ImageInlineProcessor(LinkInlineProcessor): ...

class ReferenceInlineProcessor(LinkInlineProcessor):
    NEWLINE_CLEANUP_RE: ClassVar[re.Pattern[str]]
    def evalId(self, data, index, text): ...
    def makeTag(self, href, title, text): ...

class ShortReferenceInlineProcessor(ReferenceInlineProcessor): ...
class ImageReferenceInlineProcessor(ReferenceInlineProcessor): ...
class AutolinkInlineProcessor(InlineProcessor): ...
class AutomailInlineProcessor(InlineProcessor): ...
