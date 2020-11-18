from hypothesis import given
from hypothesis.strategies import characters, text

import lzw


@given(x=text(characters(max_codepoint=255)))
def test_property(x):
	assert lzw.decompress(lzw.compress(x)) == x


test_property()
