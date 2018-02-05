import threading
import urllib2

class BackgroundStreamSaver(threading.Thread):
    def __init__(self, url='', file_path='', chunk_size=8 * 1024):
        self._url, self._cookie = url.split('|Cookie=')
        self._file_path = file_path
        self._chunk_size = chunk_size
        threading.Thread.__init__(self, target=self.stream_save)

    def stream_save(self):
        if self._url and self._file_path:
            request = urllib2.Request(self._url)
            request.add_header('Cookie', self._cookie)
            response = urllib2.urlopen(request)
            if (response.code == 200):
                with open(self._file_path, 'wb') as file_handle:
                    while True:
                        buf = response.read(self._chunk_size)
                        if not buf:
                            break
                        file_handle.write(buf)


