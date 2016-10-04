from cuda_lint import Linter, util


class Ruby(Linter):
    """Provides an interface to ruby -wc."""

    syntax = 'Ruby'
    cmd = 'ruby -wc'
    regex = (
        r'^(?P<file>.+?):(?P<line>\d+): (?:(?P<error>.*?error)|(?P<warning>warning))[,:] (?P<message>[^\r\n]+)\r?\n'  # nopep8
        r'(?:^[^\r\n]+\r?\n^(?P<col>.*?)\^)?')
    multiline = True
    comment_re = r'\s*#'

    def split_match(self, match):
        """
        Return the components of the match.

        We override this because unrelated library files can throw errors,
        and we only want errors from the linted file.

        """

        if match:
            if match.group('file') != '-':
                match = None

        return super(Ruby,self).split_match(match)
