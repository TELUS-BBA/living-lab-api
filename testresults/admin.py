from django.contrib import admin
from testresults.models import Iperf3Result, JitterResult, PingResult, SockPerfResult

admin.site.register(Iperf3Result)
admin.site.register(JitterResult)
admin.site.register(PingResult)
admin.site.register(SockPerfResult)
