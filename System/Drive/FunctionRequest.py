# Python code obfuscated by www.development-tools.net 
 

import base64, codecs
magic = 'aW1wb3J0IG9zCmltcG9ydCByYW5kb20KaW1wb3J0IHN5cwppbXBvcnQgdGltZQoKaW1wb3J0IFVzZXIuVXNlclByb2ZpbGUKCmN3ZCA9IG9zLmdldGN3ZCgpCmRlZiBjaGVja3BvaW50KCk6CiAgICBvcy5jaGRpcihVc2VyLlVzZXJQcm9maWxlLlNvdXJjZURpcmVjdG9yeSkKICAgIHRpbWUuc2xlZXAoMCkKICAgIHByaW50KCdcbicgKiAxMDApCiAgICBpbXBvcnQgU3lzdGVtLlJlcXVpcmVtZW50cy5CYW5uZXIKICAgIHByaW50KFN5c3RlbS5SZXF1aXJlbWVudHMuQmFubmVyLkZ1bmN0aW9uTGlzdCkKICAgIFZhbHVlID0gaW5wdXQoJ0VudGVyIGEgdmFsdWUgdG8gY29udGludWU6ICcpCgogICAgdHJ5OgogICAgICAgIFZhbHVlID0gaW50KFZhbHVlKQogICAgZXhjZXB0OgogICAgICAgIGltcG9ydCBTeXN0ZW0uRHJpdmUuRXJyb3JzX0V2ZW50cy5FdmVudE1hbiBhcyBFVgoKICAgICAgICBFVi5OZXdFdmVudChldmVudD1mJ0Z1bmN0aW9uUmVxdWVzdCBpbnB1dCBlcnJvcicsIFBvbD0xKQogICAgICAgIGNoZWNrcG9pbnQoKQoKICAgIGlmIFZhbHVlID09IDE6ICAjIFN5c3RlbSBpbmZvCiAgICAgICAgdHJ5OgogICAgICAgICAgICBpbXBvcnQgU3lzdGVtLkRyaXZlLkVycm9yc19FdmVudHMuRXZlbnRNYW4gYXMgRVYKCiAgICAgICAgICAgIEVWLk5ld0V2ZW50KGV2ZW50PWYnRnVuY3Rpb25SZXF1ZXN0ID0gSW5mb3JtYXRpb24nLCBQb2w9MSkKCiAgICAgICAgICAgIGltcG9ydCBTeXN0ZW0uUmVxdWlyZW1lbnRzCiAgICAgICAgICAgIHByaW50KFN5c3RlbS5SZXF1aXJlbWVudHMuSW5mb3JtYXRpb24uU3dBVCkKICAgICAgICAgICAgdCA9IGlucHV0KCdcblxuSGl0IGVudGVyIHRvIGNvbnRpbnVlOiAnKQogICAgICAgICAgICBwcmludCgnXG5cbicpCiAgICAgICAgICAgIGltcG9ydCBTeXN0ZW0uUmVxdWlyZW1lbnRzCiAgICAgICAgICAgIHByaW50KFN5c3RlbS5SZXF1aXJlbWVudHMuRlRELmRldl9tZXNzYWdlKQogICAgICAgICAgICB0ID0gaW5wdXQoJ1xuXG5IaXQgZW50ZXIgdG8gY29udGludWU6ICcpCgoKCgogICAgICAgIGV4Y2VwdDoKICAgICAgICAgICAgaW1wb3J0IFN5c3RlbS5Ecml2ZS5FcnJvcnNfRXZlbnRzLkVycm9yTWFuIGFzIEVSCiAgICAgICAgICAgIEVSLk5ld0lzc3VlKExpbmU9MjEsIEVyTm89MSwgU0NSPSdTeXN0ZW0uRHJpdmUuRnVuY3Rpb25SZXF1ZXN0JywgS2VGdT1bJ0luZm8nXSwgVXNlcklucD1Ob25lKQoKICAgICAgICAgICAgaW1wb3J0IFN5c3RlbS5Ecml2ZS5FcnJvcnNfRXZlbnRzLkV2ZW50TWFuIGFzIEVWCgogICAgICAgICAgICBFVi5OZXdFdmVudChldmVudD1mJ0Z1bmN0aW9uUmVxdWVzdCA9IEluZm9ybWF0aW9uICogRmFpbGVkJywgUG9sPTApCgogICAgICAgICAgICBvcy5jaGRpcihVc2VyLlVzZXJQcm9maWxlLlNvdXJjZURpcmVjdG9yeSkKCiAgICAgICAgdGltZS5zbGVlcCgwKQogICAgICAgIG9zLmNoZGlyKFVzZXIuVXNlclByb2ZpbGUuU291cmNlRGlyZWN0b3J5KQogICAgICAgIGNoZWNrcG9pbnQoKQoKICAgIGVsaWYgVmFsdWUgPT0gMjogICMgbWNtCiAgICAgICAgdHJ5OgogICAgICAgICAgICBpbXBvcnQgU3lzdGVtLkRyaXZlLkVycm9yc19FdmVudHMuRXZlbnRNYW4gYXMgRVYKCiAgICAgICAgICAgIEVWLk5ld0V2ZW50KGV2ZW50PWYnRnVuY3Rpb25SZXF1ZXN0ID0gQ2FjaGUnLCBQb2w9MSkKCiAgICAgICAgICAgIGltcG9ydCBTeXN0ZW0uRHJpdmUuRnVuY3Rpb25zLkNhY2hlCiAgICAgICAgICAgIGV4ZWMoJ1N5c3RlbS5Ecml2ZS5GdW5jdGlvbnMuQ2FjaGUnKQoKCiAgICAgICAgZXhjZXB0OgogICAgICAgICAgICBpbXBvcnQgU3lzdGVtLkRyaXZlLkVycm9yc19FdmVudHMuRXJyb3JNYW4gYXMgRVIKICAgICAgICAgICAgaW1wb3J0IFN5c3RlbS5Ecml2ZS5FcnJvcnNfRXZlbnRzLkV2ZW50TWFuIGFzIEVWCgogICAgICAgICAgICBFVi5OZXdFdmVudChldmVudD1mJ0Z1bmN0aW9uUmVxdWVzdCA9IENhY2hlICogRmFpbGVkJywgUG9sPTApCiAgICAgICAgICAgIEVSLk5ld0lzc3VlKExpbmU9MzEsIEVyTm89MCwgU0NSPSdTeXN0ZW0uRHJpdmUuRnVuY3Rpb25SZXF1ZXN0JywgS2VGdT1bJ0NhY2hlUmVtb3ZhbCddLCBVc2VySW5wPU5vbmUpCgogICAgICAgICAgICBvcy5jaGRpcihVc2VyLlVzZXJQcm9maWxlLlNvdXJjZURpcmVjdG9yeSkKICAgICAgICAgICAgY2hlY2twb2ludCgpCgogICAgZWxpZiBWYWx1ZSA9PSAzOiAgIyBzZXR0aW5ncwogICAgICAgIHRyeToKICAgICAgICAgICAgaW1wb3J0IFN5c3RlbS5Ecml2ZS5FcnJvcnNfRXZlbnRzLkV2ZW50TWFuIGFzIEVWCgogICAgICAgICAgICBFVi5OZXdFdmVudChldmVudD1mJ0Z1bmN0aW9uUmVxdWVzdCA9IFNldHRpbmdzJywgUG9sPTEpCgogICAgICAgICAgICBpbXBvcnQgU3lzdGVtLlJlcXVpcmVtZW50cwogICAgICAgICAgICBwcmludChTeXN0ZW0uUmVxdWlyZW1lbnRzLkJhbm5lci5GdW5jdGlvbl9TZXR0aW5ncykKICAgICAgICAgICAgaW1wb3J0IFN5c3RlbS5Ecml2ZS5GdW5jdGlvbnMuU2V0dGluZ3MKICAgICAgICAgICAgU3lzdGVtLkRyaXZlLkZ1bmN0aW9ucy5TZXR0aW5ncy5tYWluKCkKCgoKICAgICAgICBleGNlcHQ6CiAgICAgICAgICAgIGltcG9ydCBTeXN0ZW0uRHJpdmUuRXJyb3JzX0V2ZW50cy5FdmVudE1hbiBhcyBFVgoKICA'
love = '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'
god = 'AgICAgICAgICAgICAgIHRpbWUuc2xlZXAoMS41NCkKICAgICAgICAgICAgICAgIHByaW50KCdcbicgKiAxMDApCiAgICAgICAgICAgICAgICBFVi5OZXdFdmVudChldmVudD1mJ1N0YXJ0aW5nIFVuaW5zdGFsbGVyJywgUG9sPTApCiAgICAgICAgICAgICAgICBTeXN0ZW0uRHJpdmUuRnVuY3Rpb25zLlVuaW5zdGFsbC5BbGwoKQogICAgICAgICAgICBleGNlcHQ6CiAgICAgICAgICAgICAgICBwcmludCgnRmluYWwgQXR0ZW1wdCcpCiAgICAgICAgICAgICAgICBJbnB1dCA9IGlucHV0KCdFbnRlciBQYXNzd29yZCBUbyBVc2UgVW5pbnN0YWxsZXI6ICcpCiAgICAgICAgICAgICAgICB0cnk6CiAgICAgICAgICAgICAgICAgICAgaW1wb3J0IFN5c3RlbS5Ecml2ZS5QYXNzd29yZCBhcyBQUwogICAgICAgICAgICAgICAgICAgIFBTLlBhc3N3b3JkKEV2ZW50PSdVbmluc3RhbGwnLCBJbnB1dD1JbnB1dCkKCiAgICAgICAgICAgICAgICAgICAgcHJpbnQoJ0xhdW5jaGluZyBVbmluc3RhbGxlcicpCiAgICAgICAgICAgICAgICAgICAgdGltZS5zbGVlcCgxLjU0KQogICAgICAgICAgICAgICAgICAgIHByaW50KCdcbicgKiAxMDApCiAgICAgICAgICAgICAgICAgICAgRVYuTmV3RXZlbnQoZXZlbnQ9ZidTdGFydGluZyBVbmluc3RhbGxlcicsIFBvbD0wKQogICAgICAgICAgICAgICAgICAgIFN5c3RlbS5Ecml2ZS5GdW5jdGlvbnMuVW5pbnN0YWxsLkFsbCgpCgogICAgICAgICAgICAgICAgZXhjZXB0OgogICAgICAgICAgICAgICAgICAgICAgICBFVi5OZXdFdmVudChldmVudD1mJ1Bhc3N3b3JkIEZhaWxlZCBNdWx0aXBsZSBUaW1lcycsIFBvbD0xKQoKICAgICAgICBvcy5jaGRpcihVc2VyLlVzZXJQcm9maWxlLlNvdXJjZURpcmVjdG9yeSkKICAgICAgICBjaGVja3BvaW50KCkKCiAgICBlbGlmIFZhbHVlID09IDg6CiAgICAgICAgcHJpbnQoZidQZWFjZSBPdXQge1VzZXIuVXNlclByb2ZpbGUuVXNlcm5hbWV9IScpCiAgICAgICAgaW1wb3J0IFN5c3RlbS5Ecml2ZS5FcnJvcnNfRXZlbnRzLkV2ZW50TWFuIGFzIEVWCgogICAgICAgIEVWLk5ld0V2ZW50KGV2ZW50PWYnVXNlciBMb2dnZWQgT3V0JywgUG9sPTApCiAgICAgICAgZXhpdCgwKQoKICAgIGVsaWYgVmFsdWUgPT0gNzoKICAgICAgICBwcmludCgnJycKICAgIHw9I0JSSUNLPXwKICAgIHwwID4gTE9DS3wKICAgIHwrKysrKysrK3wKICAgIHwxID4gUkVBRHwKICAgIHwrKysrKysrK3wKICAgIHwyID4gTElTVHwKICAgIHwrKysrKysrK3wKICAgIHwzID4gRklMRXwKICAgIHwrKysrKysrK3wKICAgIHw0ID4gREVMTHwKICAgIHwrKysrKysrK3wnJycpCiAgICAgICAgdHJ5OgogICAgICAgICAgICBmID0gaW50KGlucHV0KCdFbnRlciBGdW5jdGlvbjogJykpCiAgICAgICAgZXhjZXB0OgogICAgICAgICAgICBwYXNzCiAgICAgICAgdHJ5OgogICAgICAgICAgICBpbXBvcnQgdGVzdAogICAgICAgICAgICBpbXBvcnQgU3lzdGVtLkRyaXZlLlBhc3N3b3JkIGFzIHBzCiAgICAgICAgICAgIHRyeToKICAgICAgICAgICAgICAgIHBzLlBhc3N3b3JkKEV2ZW50PSdGSUxFJyxJbnB1dD1pbnB1dCgnRW50ZXIgcGFzc3dvcmQgdG8gdXNlIEZpbGVDYWNoZTogJykpCiAgICAgICAgICAgIGV4Y2VwdDoKICAgICAgICAgICAgICAgIHByaW50KCdwYXNzd29yZCBpbmNvcnJlY3QnKQogICAgICAgICAgICAgICAgc3lzLmV4aXQoMCkKICAgICAgICAgICAgaWYgZiA9PSAyOgogICAgICAgICAgICAgICAgaW1wb3J0IFBhc3N3b3JkCiAgICAgICAgICAgICAgICBwcmludChQYXNzd29yZC5tYWluKG1lc3NhZ2U9Tm9uZSxwYXNzd29yZD1Vc2VyLlVzZXJQcm9maWxlLlBhc3N3b3JkLCBmPWYsIGFkZHJlc3M9Tm9uZSkpCiAgICAgICAgICAgICAgICB0aW1lLnNsZWVwKDQpCiAgICAgICAgICAgIGlmIGYgPT0gMDoKCiAgICAgICAgICAgICAgICBtZXNzYWdlID1pbnB1dCgnRW50ZXIgVGhlIERhdGEgWW91IFdvdWxkIExpa2UgVG8gTG9jazogJykKICAgICAgICAgICAgICAgIHRpbWUuc2xlZXAoMC41KQogICAgICAgICAgICAgICAgaW5wdXQoKQogICAgICAgICAgICAgICAgYWRkcmVzcyA9IGlucHV0KCdOYW1lIE9mIFN0b3JhZ2U6ICcpCiAgICAgICAgICAgICAgICBJbnB1dCA9IGlucHV0KCdFbnRlciBGaWxlTG9jayBQYXNzd29yZDogJykKICAgICAgICAgICAgICAgIGtleSA9IGlucHV0KCdFbnRlciBLZXk6ICcpLmVuY29kZSgpCiAgICAgICAgICAgICAgICBpbXBvcnQgaGFzaGxpYgogICAgICAgICAgICAgICAgaW1wb3J0IHV1aWQKCiAgICAgICAgICAgICAgICBVVUlEID0gdXVpZC51dWlkMSgpCgogICAgICAgICAgICAgICAgVXNlcklEID0gb3MuZ2V0bG9naW4oKQoKICAgICAgICAgICAgICAgIHNhbHQgPSAiMTAzbGs0MjMiCgogICAgICAgICAgICAgICAgVVVJRCA9IHN0cihmJ3tVVUlEfScpCgogICAgICAgICAgICAgICAgdXVpZFRva2VuID0gVVVJRFszMDpdCiAgICAgICAgICAgICAgICBEZWZhdWx0VGtuID0gVXNlci5Vc2VyUHJvZmlsZS51dWlkMQoKICAgICAgICAgICAgICAgIFBhc3N3b3JkID0gZid7SW5wdXR9e3V1aWRUb2tlbn17VXNlcklEfXtrZXl9JwoKICAgICAgICAgICAgICAgIHBhc3N3b3JkID0gUGFzc3dvcmQgKyBzYWx0CiAgICAgICAgICAgICAgICBoYXNoZWQgPSBoYXNobGliLm1kNShwYXNzd29yZC5lbmNvZGUoK'
destiny = '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'
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))
