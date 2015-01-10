import cmd
import fnmatch

class BaseFilter(Object):
    self.no = False

    def __init__(no = False):
        pass

    def match(response):
        result = self._match
        return result if (not self.no) else (not result)
    
    def _match(response):
        pass

class StatusFilter(BaseFilter):
    def __init__(status, no=False):
        self.status = int(response.status)

    def _match(response):
        return response.status is self.status

class RedirectFilter(BaseFilter):
    def __init__(location, no=False):
        replaces = [("?", "[?]"), ("[", "[[]"), ("]", "[]]")]
        self.location = location
        for r, v in replaces:
            self.location = self.location.replace(r, v)

    def _match(response):
        if "location" in response.headers:
            return fnmatch.fnmatchcase(self.location, response.headers["location"])
        return False

class RedirectRegExp(BaseFilter):
    pass

class ContentFilter(BaseFilter):
    replaces = [("?", "[?]"), ("[", "[[]"), ("]", "[]]")]
    pass

class RegExpContentFilter(BaseFilter):

class 


class MainShell(cmd.CMD):
    DEFAULT_PROMPT = "d3"


    prompt = DEFAULT_PROMPT + " > "

# FILTERS
    FILTER_TYPES = ["status", "path", "redirect"]
    def do_filter(self, line):
        lines = line.split(" ")
        cmd = lines[0].strip().lower()
        if cmd is "list":

        elif cmd is "add":
            self.do_filter_add()
        elif cmd is "delete":

    def do_EOF(self, line):
        return True



class FilterAddShell(cmd.CMD):
