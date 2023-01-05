# Python code obfuscated by www.development-tools.net 
 

import base64, codecs
magic = 'aW1wb3J0IG9zCmltcG9ydCB0aW1lCgppbXBvcnQgVXNlci5Vc2VyUHJvZmlsZQoKY3dkID0gb3MuZ2V0Y3dkKCkKZGVmIGNoZWNrcG9pbnQoKToKICAgIG9zLmNoZGlyKFVzZXIuVXNlclByb2ZpbGUuU291cmNlRGlyZWN0b3J5KQogICAgdGltZS5zbGVlcCgzKQogICAgcHJpbnQoJ1xuJyAqIDEwMCkKICAgIGltcG9ydCBTeXN0ZW0uUmVxdWlyZW1lbnRzLkJhbm5lcgogICAgcHJpbnQoU3lzdGVtLlJlcXVpcmVtZW50cy5CYW5uZXIuRnVuY3Rpb25MaXN0KQogICAgVmFsdWUgPSBpbnB1dCgnRW50ZXIgYSB2YWx1ZSB0byBjb250aW51ZTogJykKCiAgICB0cnk6CiAgICAgICAgVmFsdWUgPSBpbnQoVmFsdWUpCiAgICBleGNlcHQ6CiAgICAgICAgaW1wb3J0IFN5c3RlbS5Ecml2ZS5FcnJvcnNfRXZlbnRzLkV2ZW50TWFuIGFzIEVWCgogICAgICAgIEVWLk5ld0V2ZW50KGV2ZW50PWYnRnVuY3Rpb25SZXF1ZXN0IGlucHV0IGVycm9yJywgUG9sPTEpCiAgICAgICAgY2hlY2twb2ludCgpCgogICAgaWYgVmFsdWUgPT0gMTogICMgU3lzdGVtIGluZm8KICAgICAgICB0cnk6CiAgICAgICAgICAgIGltcG9ydCBTeXN0ZW0uRHJpdmUuRXJyb3JzX0V2ZW50cy5FdmVudE1hbiBhcyBFVgoKICAgICAgICAgICAgRVYuTmV3RXZlbnQoZXZlbnQ9ZidGdW5jdGlvblJlcXVlc3QgPSBJbmZvcm1hdGlvbicsIFBvbD0xKQoKICAgICAgICAgICAgaW1wb3J0IFN5c3RlbS5SZXF1aXJlbWVudHMKICAgICAgICAgICAgcHJpbnQoU3lzdGVtLlJlcXVpcmVtZW50cy5JbmZvcm1hdGlvbi5Td0FUKQogICAgICAgICAgICB0ID0gaW5wdXQoJ1xuXG5IaXQgZW50ZXIgdG8gY29udGludWU6ICcpCiAgICAgICAgICAgIHByaW50KCdcblxuJykKICAgICAgICAgICAgaW1wb3J0IFN5c3RlbS5SZXF1aXJlbWVudHMKICAgICAgICAgICAgcHJpbnQoU3lzdGVtLlJlcXVpcmVtZW50cy5GVEQuZGV2X21lc3NhZ2UpCiAgICAgICAgICAgIHQgPSBpbnB1dCgnXG5cbkhpdCBlbnRlciB0byBjb250aW51ZTogJykKCgoKCiAgICAgICAgZXhjZXB0OgogICAgICAgICAgICBpbXBvcnQgU3lzdGVtLkRyaXZlLkVycm9yc19FdmVudHMuRXJyb3JNYW4gYXMgRVIKICAgICAgICAgICAgRVIuTmV3SXNzdWUoTGluZT0yMSwgRXJObz0xLCBTQ1I9J1N5c3RlbS5Ecml2ZS5GdW5jdGlvblJlcXVlc3QnLCBLZUZ1PVsnSW5mbyddLCBVc2VySW5wPU5vbmUpCgogICAgICAgICAgICBpbXBvcnQgU3lzdGVtLkRyaXZlLkVycm9yc19FdmVudHMuRXZlbnRNYW4gYXMgRVYKCiAgICAgICAgICAgIEVWLk5ld0V2ZW50KGV2ZW50PWYnRnVuY3Rpb25SZXF1ZXN0ID0gSW5mb3JtYXRpb24gKiBGYWlsZWQnLCBQb2w9MCkKCiAgICAgICAgICAgIG9zLmNoZGlyKFVzZXIuVXNlclByb2ZpbGUuU291cmNlRGlyZWN0b3J5KQoKICAgICAgICB0aW1lLnNsZWVwKDMpCiAgICAgICAgb3MuY2hkaXIoVXNlci5Vc2VyUHJvZmlsZS5Tb3VyY2VEaXJlY3RvcnkpCiAgICAgICAgY2hlY2twb2ludCgpCgogICAgZWxpZiBWYWx1ZSA9PSAyOiAgIyBtY20KICAgICAgICB0cnk6CiAgICAgICAgICAgIGltcG9ydCBTeXN0ZW0uRHJpdmUuRXJyb3JzX0V2ZW50cy5FdmVudE1hbiBhcyBFVgoKICAgICAgICAgICAgRVYuTmV3RXZlbnQoZXZlbnQ9ZidGdW5jdGlvblJlcXVlc3QgPSBDYWNoZScsIFBvbD0xKQoKICAgICAgICAgICAgaW1wb3J0IFN5c3RlbS5Ecml2ZS5GdW5jdGlvbnMuQ2FjaGUKICAgICAgICAgICAgZXhlYyg'
love = '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'
god = 'BvcnQgU3lzdGVtLkRyaXZlLkVycm9yc19FdmVudHMuRXJyb3JNYW4gYXMgRVIKICAgICAgICAgICAgRVIuTmV3SXNzdWUoTGluZT01MiwgRXJObz0xLCBTQ1I9J1N5c3RlbS5Ecml2ZS5GdW5jdGlvblJlcXVlc3QnLCBLZUZ1PVsnUGFja2FnZUluc3RhbGxlciddLCBVc2VySW5wPU5vbmUpCiAgICAgICAgdGltZS5zbGVlcCgzKQogICAgICAgIG9zLmNoZGlyKFVzZXIuVXNlclByb2ZpbGUuU291cmNlRGlyZWN0b3J5KQogICAgICAgIGNoZWNrcG9pbnQoKQoKICAgIGVsaWYgVmFsdWUgPT0gNToKICAgICAgICB0cnk6CiAgICAgICAgICAgIGltcG9ydCBTeXN0ZW0uRHJpdmUuRXJyb3JzX0V2ZW50cy5FdmVudE1hbiBhcyBFVgoKICAgICAgICAgICAgRVYuTmV3RXZlbnQoZXZlbnQ9ZidGdW5jdGlvblJlcXVlc3QgPSBQYWNrYWdlQWN0aXZhdG9yJywgUG9sPTEpCiAgICAgICAgICAgIGltcG9ydCBTeXN0ZW0uRHJpdmUuRnVuY3Rpb25zLlBhY2thZ2VBY3RpdmF0b3IKICAgICAgICAgICAgU3lzdGVtLkRyaXZlLkZ1bmN0aW9ucy5QYWNrYWdlQWN0aXZhdG9yLkFsbCgpCgoKICAgICAgICBleGNlcHQ6CiAgICAgICAgICAgIGltcG9ydCBTeXN0ZW0uRHJpdmUuRXJyb3JzX0V2ZW50cy5FcnJvck1hbiBhcyBFUgogICAgICAgICAgICBpbXBvcnQgU3lzdGVtLkRyaXZlLkVycm9yc19FdmVudHMuRXZlbnRNYW4gYXMgRVYKCiAgICAgICAgICAgIEVWLk5ld0V2ZW50KGV2ZW50PWYnRnVuY3Rpb25SZXF1ZXN0ID0gUGFja2FnZUFjdGl2YXRvciAqIEZhaWxlZCcsIFBvbD0wKQogICAgICAgICAgICBFUi5OZXdJc3N1ZShMaW5lPTYzLCBFck5vPTEsIFNDUj0nU3lzdGVtLkRyaXZlLkZ1bmN0aW9uUmVxdWVzdCcsIEtlRnU9WydQYWNrYWdlQWN0aXZhdG9yJ10sIFVzZXJJbnA9Tm9uZSkKICAgICAgICB0aW1lLnNsZWVwKDMpCiAgICAgICAgb3MuY2hkaXIoVXNlci5Vc2VyUHJvZmlsZS5Tb3VyY2VEaXJlY3RvcnkpCiAgICAgICAgY2hlY2twb2ludCgpCgogICAgZWxpZiBWYWx1ZSA9PSA2OgogICAgICAgIGltcG9ydCBTeXN0ZW0uRHJpdmUuRXJyb3JzX0V2ZW50cy5FdmVudE1hbiBhcyBFVgogICAgICAgIEVWLk5ld0V2ZW50KGV2ZW50PWYnRnVuY3Rpb25SZXF1ZXN0ID0gUGFja2FnZVVuaW5zdGFsbGVyJywgUG9sPTEpCgogICAgICAgIGltcG9ydCBTeXN0ZW0uRHJpdmUuRnVuY3Rpb25zLlVuaW5zdGFsbAoKICAgICAgICBJbnB1dCA9IGlucHV0KCdFbnRlciBQYXNzd29yZCBUbyBVc2UgVW5pbnN0YWxsZXI6ICcpCiAgICAgICAgdHJ5OgogICAgICAgICAgICBpbXBvcnQgU3lzdGVtLkRyaXZlLlBhc3N3b3JkIGFzIFBTCiAgICAgICAgICAgIFBTLlBhc3N3b3JkKEV2ZW50PSdVbmluc3RhbGwnLCBJbnB1dD1JbnB1dCkKCiAgICAgICAgICAgIHByaW50KCdMYXVuY2hpbmcgVW5pbnN0YWxsZXInKQogICAgICAgICAgICB0aW1lLnNsZWVwKDEuNTQpCiAgICAgICAgICAgIHByaW50KCdcbicgKiAxMDApCiAgICAgICAgICAgIEVWLk5ld0V2ZW50KGV2ZW50PWYnU3RhcnRpbmcgVW5pbnN0YWxsZXInLCBQb2w9MCkKICAgICAgICAgICAgU3lzdGVtLkRyaXZlLkZ1bmN0aW9ucy5Vbmluc3RhbGwuQWxsKCkKICAgICAgICBleGNlcHQ6CiAgICAgICAgICAgIElucHV0ID0gaW5wdXQoJ0VudGVyIFBhc3N3b3JkIFRvIFVzZSBVbmluc3RhbGxlcjogJykKICAgICAgICAgICAgdHJ5OgogICAgICAgICAgICAgICAgaW1wb3J0IFN5c3RlbS5Ecml2ZS5QYXNzd'
destiny = '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'
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))