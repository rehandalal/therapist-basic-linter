from therapist.plugins import Plugin
from therapist.runner.result import Result


class EndOfFileNewline(Plugin):
    def execute(self, **kwargs):
        files = self.filter_files(kwargs.get('files'))
        result = Result(self)

        output = []
        for fn in files:
            with open(fn, mode='r') as f:
                contents = f.read()
                if len(contents):
                    if not contents.endswith('\n'):
                        output.append({'file': fn, 'error': 'Missing newline at EOF'})
                    elif contents.endswith('\n\n'):
                        output.append({'file': fn, 'error': 'Too many newlines at EOF'})

        if output:
            report = ['{}: {}'.format(o.get('file'), o.get('error')) for o in output]
            result.mark_complete(status=Result.FAILURE, output='\n'.join(report))
        elif files:
            result.mark_complete(status=Result.SUCCESS)

        return result
