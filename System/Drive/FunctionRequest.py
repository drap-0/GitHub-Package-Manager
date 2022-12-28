
import base64, codecs
magic = 'aW1wb3J0IG9zCmltcG9ydCB0aW1lCgppbXBvcnQgVXNlci5Vc2VyUHJvZmlsZQoKY3dkID0gb3MuZ2V0Y3dkKCkKZGVmIGNoZWNrcG9pbnQoKToKICAgIG9zLmNoZGlyKFVzZXIuVXNlclByb2ZpbGUuU291cmNlRGlyZWN0b3J5KQogICAgdGltZS5zbGVlcCgzKQogICAgcHJpbnQoJ1xuJyAqIDEwMCkKICAgIGltcG9ydCBTeXN0ZW0uUmVxdWlyZW1lbnRzLkJhbm5lcgogICAgcHJpbnQoU3lzdGVtLlJlcXVpcmVtZW50cy5CYW5uZXIuRnVuY3Rpb25MaXN0KQogICAgVmFsdWUgPSBpbnB1dCgnRW50ZXIgYSB2YWx1ZSB0byBjb250aW51ZTogJykKCiAgICB0cnk6CiAgICAgICAgVmFsdWUgPSBpbnQoVmFsdWUpCiAgICBleGNlcHQ6CiAgICAgICAgaW1wb3J0IFN5c3RlbS5Ecml2ZS5FcnJvcnNfRXZlbnRzLkV2ZW50TWFuIGFzIEVWCgogICAgICAgIEVWLk5ld0V2ZW50KGV2ZW50PWYnRnVuY3Rpb25SZXF1ZXN0IGlucHV0IGVycm9yJywgUG9sPTEpCiAgICAgICAgY2hlY2twb2ludCgpCgogICAgaWYgVmFsdWUgPT0gMTogICMgU3lzdGVtIGluZm8KICAgICAgICB0cnk6CiAgICAgICAgICAgIGltcG9ydCBTeXN0ZW0uRHJpdmUuRXJyb3JzX0V2ZW50cy5FdmVudE1hbiBhcyBFVgoKICAgICAgICAgICAgRVYuTmV3RXZlbnQoZXZlbnQ9ZidGdW5jdGlvblJlcXVlc3QgPSBJbmZvcm1hdGlvbicsIFBvbD0xKQoKICAgICAgICAgICAgaW1wb3J0IFN5c3RlbS5SZXF1aXJlbWVudHMKICAgICAgICAgICAgcHJpbnQoU3lzdGVtLlJlcXVpcmVtZW50cy5JbmZvcm1hdGlvbi5Td0FUKQogICAgICAgICAgICB0ID0gaW5wdXQoJ1xuXG5IaXQgZW50ZXIgdG8gY29udGludWU6ICcpCiAgICAgICAgICAgIHByaW50KCdcblxuJykKICAgICAgICAgICAgaW1wb3J0IFN5c3RlbS5SZXF1aXJlbWVudHMKICAgICAgICAgICAgcHJpbnQoU3lzdGVtLlJlcXVpcmVtZW50cy5GVEQuZGV2X21lc3NhZ2UpCiAgICAgICAgICAgIHQgPSBpbnB1dCgnXG5cbkhpdCBlbnRlciB0byBjb250aW51ZTogJykKCgoKCiAgICAgICAgZXhjZXB0OgogICAgICAgICAgICBpbXBvcnQgU3lzdGVtLkRyaXZlLkVycm9yc19FdmVudHMuRXJyb3JNYW4gYXMgRVIKICAgICAgICAgICAgRVIuTmV3SXNzdWUoTGluZT0yMSwgRXJObz0xLCBTQ1I9J1N5c3RlbS5Ecml2ZS5GdW5jdGlvblJlcXVlc3QnLCBLZUZ1PVsnSW5mbyddLCBVc2VySW5wPU5vbmUpCgogICAgICAgICAgICBpbXBvcnQgU3lzdGVtLkRyaXZlLkVycm9yc19FdmVudHMuRXZlbnRNYW4gYXMgRVYKCiAgICAgICAgICAgIEVWLk5ld0V2ZW50KGV2ZW50PWYnRnVuY3Rpb25SZXF1ZXN0ID0gSW5mb3JtYXRpb24gKiBGYWlsZWQnLCBQb2w9MCkKCiAgICAgICAgICAgIG9zLmNoZGlyKFVzZXIuVXNlclByb2ZpbGUuU291cmNlRGlyZWN0b3J5KQoKICAgICAgICB0aW1lLnNsZWVwKDMpCiAgICAgICAgb3MuY2hkaXIoVXNlci5Vc2VyUHJvZmlsZS5Tb3VyY2VEaXJlY3RvcnkpCiAgICAgICAgY2hlY2twb2ludCgpCgogICAgZWxpZiBWYWx1ZSA9PSAyOiAgIyBtY20KICAgICAgICB0cnk6CiAgICAgICAgICAgIGltcG9ydCBTeXN0ZW0uRHJpdmUuRXJyb3JzX0V2ZW50cy5FdmVudE1hbiBhcyBFVgoKICAgICAgICAgICAgRVYuTmV3RXZlbnQoZXZlbnQ9ZidGdW5jdGlvblJlcXVlc3QgPSBDYWNoZScsIFBvbD0xKQoKICAgICAgICAgICAgaW1wb3J0IFN5c3RlbS5Ecml2ZS5DYWNoZQogICAgICAgICAgICBleGVjKCdTeXN0ZW0uRHJpdmUuQ2FjaGUnKQoKCiAgICAgICAgZXhjZXB0OgogICAgICAgICAgICBpbXBvcnQgU3lzdGVtLkRyaXZlLkVycm9yc19FdmVudHMuRXJyb3JNYW4gYXMgRVIKICAgICAgICAgICAgaW1wb3J0IFN5c3RlbS'
love = '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'
god = 'aW50KCkKCiAgICBlbGlmIFZhbHVlID09IDU6CiAgICAgICAgdHJ5OgogICAgICAgICAgICBpbXBvcnQgU3lzdGVtLkRyaXZlLkVycm9yc19FdmVudHMuRXZlbnRNYW4gYXMgRVYKCiAgICAgICAgICAgIEVWLk5ld0V2ZW50KGV2ZW50PWYnRnVuY3Rpb25SZXF1ZXN0ID0gUGFja2FnZUFjdGl2YXRvcicsIFBvbD0xKQogICAgICAgICAgICBpbXBvcnQgU3lzdGVtLkRyaXZlLkZ1bmN0aW9ucy5QYWNrYWdlQWN0aXZhdG9yCiAgICAgICAgICAgIFN5c3RlbS5Ecml2ZS5GdW5jdGlvbnMuUGFja2FnZUFjdGl2YXRvci5BbGwoKQoKCiAgICAgICAgZXhjZXB0OgogICAgICAgICAgICBpbXBvcnQgU3lzdGVtLkRyaXZlLkVycm9yc19FdmVudHMuRXJyb3JNYW4gYXMgRVIKICAgICAgICAgICAgaW1wb3J0IFN5c3RlbS5Ecml2ZS5FcnJvcnNfRXZlbnRzLkV2ZW50TWFuIGFzIEVWCgogICAgICAgICAgICBFVi5OZXdFdmVudChldmVudD1mJ0Z1bmN0aW9uUmVxdWVzdCA9IFBhY2thZ2VBY3RpdmF0b3IgKiBGYWlsZWQnLCBQb2w9MCkKICAgICAgICAgICAgRVIuTmV3SXNzdWUoTGluZT02MywgRXJObz0xLCBTQ1I9J1N5c3RlbS5Ecml2ZS5GdW5jdGlvblJlcXVlc3QnLCBLZUZ1PVsnUGFja2FnZUFjdGl2YXRvciddLCBVc2VySW5wPU5vbmUpCiAgICAgICAgdGltZS5zbGVlcCgzKQogICAgICAgIG9zLmNoZGlyKFVzZXIuVXNlclByb2ZpbGUuU291cmNlRGlyZWN0b3J5KQogICAgICAgIGNoZWNrcG9pbnQoKQoKICAgIGVsaWYgVmFsdWUgPT0gNjoKICAgICAgICBpbXBvcnQgU3lzdGVtLkRyaXZlLkVycm9yc19FdmVudHMuRXZlbnRNYW4gYXMgRVYKICAgICAgICBFVi5OZXdFdmVudChldmVudD1mJ0Z1bmN0aW9uUmVxdWVzdCA9IFBhY2thZ2VVbmluc3RhbGxlcicsIFBvbD0xKQoKICAgICAgICBpbXBvcnQgU3lzdGVtLkRyaXZlLkZ1bmN0aW9ucy5Vbmluc3RhbGwKCiAgICAgICAgUGFzc3dvcmQgPSBpbnB1dCgnRW50ZXIgUGFzc3dvcmQgVG8gVXNlIFVuaW5zdGFsbGVyOiAnKQogICAgICAgIHRyeToKICAgICAgICAgICAgaW1wb3J0IGhhc2hsaWIKICAgICAgICAgICAgc2FsdCA9ICI5bGsiCiAgICAgICAgICAgIGRhdGFCYXNlX3Bhc3N3b3JkID0gUGFzc3dvcmQgKyBzYWx0CiAgICAgICAgICAgIGhhc2hlZCA9IGhhc2hsaWIubWQ1KGRhdGFCYXNlX3Bhc3N3b3JkLmVuY29kZSgpKQogICAgICAgICAgICBQYXNzd29yZCA9IGhhc2hlZC5oZXhkaWdlc3QoKQogICAgICAgICAgICBpZiBQYXNzd29yZCA9PSBVc2VyLlVzZXJQcm9maWxlLlBhc3N3b3JkOgogICAgICAgICAgICAgICAgcHJpbnQoJ0xhdW5jaGluZyBVbmluc3RhbGxlcicpCiAgICAgICAgICAgICAgICB0aW1lLnNsZWVwKDEuNTQpCiAgICAgICAgICAgICAgICBwcmludCgnXG4nICogMTAwKQogICAgICAgICAgICAgICAgRVYuTmV3RXZlbnQoZXZlbnQ9ZidTdGFydGluZyBVbmluc3RhbGxlcicsIFBvbD0wKQogICAgICAgICAgICAgICAgU3lzdGVtLkRyaXZlLkZ1bmN0aW9ucy5Vbmluc3RhbGwuQWxsKCkKCiAgICAgICAgICAgIGVsc2U6CiAgICAgICAgICAgICAgICBwcmludCgnUGFzc3dvcmQgaW5jb3JyZWN0LiBUcnkgYWdhaW4nKQogICAgICAgICAgICAgICAgUGFzc3dvcmQgPSBpbnB1dCgnRW50ZXIgUGFzc3dvcmQ6ICcpCiAgICAgICAgICAgICAgICBpbXBvcnQgaGFzaGxpYgogICAgICAgICAgICAgICAgc2FsdCA9ICI5bGsiCiAgICAgICAgICAgICAgICBkYXRhQmFzZV9wYXNzd29yZCA9IFBhc3N3b3JkICsgc2FsdAogICAgICAgICAgICAgICAgaGFzaGVkID0gaGFzaGxpYi5tZDUoZGF0YUJhc2VfcGFzc3dvcmQuZW5jb2RlKCkpCiAgICAgICAgICAgICAgICBQYXNzd29yZCA9IG'
destiny = 'uup2uyMP5bMKuxnJqyp3DbXDbtVPNtVPNtVPNtVPNtVPNtnJLtHTSmp3qipzDtCG0tIKAypv5Ip2IlHUWiMzyfMF5DLKAmq29lMQbXVPNtVPNtVPNtVPNtVPNtVPNtVPOjpzyhqPtaGTS1ozAbnJ5aVSIhnJ5mqTSfoTIlWlxXVPNtVPNtVPNtVPNtVPNtVPNtVPO0nJ1yYaAfMJIjXQRhAGDcPvNtVPNtVPNtVPNtVPNtVPNtVPNtpUWcoaDbW1khWlNdVQRjZPxXVPNtVPNtVPNtVPNtVPNtVPNtVPOSIv5BMKqSqzIhqPuyqzIhqQ1zW1A0LKW0nJ5aVSIhnJ5mqTSfoTIlWljtHT9fCGNcPvNtVPNtVPNtVPNtVPNtVPNtVPNtH3ymqTIgYxElnKMyYxM1ozA0nJ9hpl5Iozyhp3EuoTjhDJkfXPxXPvNtVPNtVPNtVPNtVPNtVPOyoUAyBtbtVPNtVPNtVPNtVPNtVPNtVPNtVUOlnJ50XPqDLKAmq29lMPOcozAipaWyL3DhVRMcozSfVTS0qTIgpUDaXDbtVPNtVPNtVPNtVPNtVPNtVPNtVSOup3A3o3WxVQ0tnJ5jqKDbW0IhqTIlVSOup3A3o3WxBvNaXDbtVPNtVPNtVPNtVPNtVPNtVPNtVTygpT9lqPObLKAboTyvPvNtVPNtVPNtVPNtVPNtVPNtVPNtp2SfqPN9VPV5oTfvPvNtVPNtVPNtVPNtVPNtVPNtVPNtMTS0LHWup2IspTSmp3qipzDtCFODLKAmq29lMPNeVUAuoUDXVPNtVPNtVPNtVPNtVPNtVPNtVPObLKAbMJDtCFObLKAboTyvYz1xAFuxLKEuDzSmMI9jLKAmq29lMP5yozAiMTHbXFxXVPNtVPNtVPNtVPNtVPNtVPNtVPODLKAmq29lMPN9VTuup2uyMP5bMKuxnJqyp3DbXDbtVPNtVPNtVPNtVPNtVPNtVPNtVTyzVSOup3A3o3WxVQ09VSImMKVhIKAypyOlo2McoTHhHTSmp3qipzD6PvNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVUOlnJ50XPqZLKIhL2ucozptIJ5coaA0LJkfMKVaXDbtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPO0nJ1yYaAfMJIjXQRhAGDcPvNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVUOlnJ50XPqpovptXvNkZQNcPvNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVRIJYx5yq0I2MJ50XTI2MJ50CJLaH3EupaEcozptIJ5coaA0LJkfMKVaYPODo2j9ZPxXVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtH3ymqTIgYxElnKMyYxM1ozA0nJ9hpl5Iozyhp3EuoTjhDJkfXPxXPvNtVPNtVPNtVPNtVPNtVPNtVPNtMJkmMGbXVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtEILhGzI3EKMyoaDbMKMyoaD9MvqDLKAmq29lMPOTLJyfMJDtGKIfqTyjoTHtITygMKZaYPODo2j9ZPxXVPNtVPNtVPOyrTAypUD6PvNtVPNtVPNtVPNtVRIJYx5yq0I2MJ50XTI2MJ50CJLaMKWlo3Vtq2y0nTyhVUIhnJ5mqTSfoPpfVSOioQ0jXDbXVPNtVPNtVPOipl5wnTEcpvuIp2IlYyImMKWDpz9znJkyYyAiqKWwMHEcpzIwqT9lrFxXVPNtVPNtVPOwnTIwn3OinJ50XPxXPvNtVPOyoTyzVSMuoUIyVQ09VQp6PvNtVPNtVPNtpUWcoaDbMvqDMJSwMFOCqKDtr1ImMKVhIKAypyOlo2McoTHhIKAypz5uoJI9VFpcPvNtVPNtVPNtnJ1jo3W0VSA5p3EyoF5Rpzy2MF5SpaWipaAsEKMyoaEmYxI2MJ50GJShVTSmVRIJPtbtVPNtVPNtVRIJYx5yq0I2MJ50XTI2MJ50CJLaIKAypvOZo2qaMJDtG3I0WljtHT9fCGNcPvNtVPNtVPNtMKucqPtjXDbXVPNtVTIfp2H6PtbtVPNtVPNtVTygpT9lqPOGrKA0MJ0hEUWcqzHhEKWlo3WmK0I2MJ50pl5SqzIhqR1uovOuplOSItbXVPNtVPNtVPOSIv5BMKqSqzIhqPuyqzIhqQ1zW0M1ozA0nJ9hHzIkqJImqPN9VRyhqzSfnJESoaElrFpfVSOioQ0kXDbXVPNtVPNtVPOcoKOipaDtH3ymqTIgYxElnKMyYxIlpz9lp19SqzIhqUZhEKWlo3WALJ4tLKZtEIVXVPNtVPNtVPOSHv5BMKqWp3A1MFuZnJ5yCGL5YPOSpx5iCGRfVSAQHw0aH3ymqTIgYxElnKMyYxM1ozA0nJ9hHzIkqJImqPpfVRgyEaH9JlqWozAipaWyL3EWoaO1qSMuoUIyW10fVSImMKWWoaN9Gz9hMFxX'
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))