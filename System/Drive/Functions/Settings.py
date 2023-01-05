# Python code obfuscated by www.development-tools.net 
 

import base64, codecs
magic = 'aW1wb3J0IG9zCgoKZGVmIG1haW4oKToKICAgIGltcG9ydCBTeXN0ZW0uUmVxdWlyZW1lbnRzLkluZm9ybWF0aW9uCiAgICBWYWx1ZSA9IGlucHV0KCdFbnRlciBhIHZhbHVlIHRvIGNvbnRpbnVlOiAnKQogICAgY3dkID0gb3MuZ2V0Y3dkKCkKICAgIHRyeToKICAgICAgICBWYWx1ZSA9IGludChWYWx1ZSkKICAgIGV4Y2VwdDoKICAgICAgICBpbXBvcnQgU3lzdGVtLkRyaXZlLkVycm9yc19FdmVudHMuRXZlbnRNYW4gYXMgRVYKICAgICAgICBFVi5OZXdFdmVudChldmVudD1mJ0lucHV0IEVycm9yJywgUG9sPTEpCgogICAgaW1wb3J0IFN5c3RlbS5Ecml2ZS5FcnJvcnNfRXZlbnRzLkV2ZW50TWFuIGFzIEVWCiAgICBFVi5OZXdFdmVudChldmVudD1mJ0xhdW5jaGluZyBTZXR0aW5ncycsIFBvbD0wKQogICAgaWYgVmFsdWUgPT0gMTogICMgSW5mbwogICAgICAgIHByaW50KFN5c3RlbS5SZXF1aXJlbWVudHMuSW5mb3JtYXRpb24uRnVuY3Rpb25zX1NldHRpbmdzKQogICAgICAgIGltcG9ydCBTeXN0ZW0uRHJpdmUuRXJyb3JzX0V2ZW50cy5FdmVudE1hbiBhcyBFVgoKICAgICAgICBFVi5OZXdFdmVudChldmVudD1mJ1NldHRpbmdzIEluZm8nLCBQb2w9MSkKCiAgICBlbGlmIFZhbHVlID09IDI6ICAgICMgVXNlciBTZXR0aW5ncwogICAgICAgIHByaW50KCcnJwogICAgICAgIDEgfCBUb2dnb'
love = 'THtEz9lL2IxVR1iMUIfMFOWoKOipaDXVPNtVPNtVPNlVUjtIT9aM2kyVRMipzAyMPOZo2qcotbtVPNtVPNtVQZtsPOHo2qaoTHtH3ymqTIgVRI2MJ50VTEcp3OfLKxtPvNtVPNtVPNtAPO8VRIhLJWfMFOQo21gLJ5xVRkcozHtFJ50MKWzLJAyPvNtVPNtVPNtWlpaXDbtVPNtVPNtVTyhpPN9VTyhpUI0XPqSoaEypvOuVUMuoUIyVUEiVTAioaEcoaIyBvpcPvNtVPNtVPNtqUW5BtbtVPNtVPNtVPNtVPOcoaNtCFOcoaDbnJ5jXDbtVPNtVPNtVTI4L2IjqQbXVPNtVPNtVPNtVPNtEILhGzI3EKMyoaDbMKMyoaD9MvqWoaO1qPOSpaWipvpfVSOioQ0kXDbXVPNtVPNtVPOcoKOipaDtH3ymqTIgYxElnKMyYxIlpz9lp19SqzIhqUZhEKMyoaEALJ4tLKZtEILXPvNtVPNtVPNtEILhGzI3EKMyoaDbMKMyoaD9MvqGrKA0MJ0tH2I0qTyhM3ZaYPODo2j9ZFxXPvNtVPNtVPNtnJLtnJ5jVQ09VQR6PvNtVPNtVPNtVPNtVTygpT9lqPOGrKA0MJ0hEUWcqzHhEaIhL3Eco25mYxMipzAyMR1iMUIfMHygpT9lqNbtVPNtVPNtVPNtVPOcoKOipaDtH3ymqTIgYxElnKMyYxIlpz9lp19SqzIhqUZhEKMyoaEALJ4tLKZtEILXPvNtVPNtVPNtVPNtVRIJYx5yq0I2MJ50XTI2MJ50CJLaGTS1ozAbnJ5aVRMipzAyMR1iMUIfMHygpT9lqPpfVSOioQ0kXDbtVPNtVPNtVPNtVPOyrTIwXPqGrKA0MJ0hEUWcqzHhEaIhL3Eco2'
god = '5zLkZvcmNlZE1vZHVsZUltcG9ydCcpCgogICAgICAgIGVsaWYgaW5wID09IDI6CiAgICAgICAgICAgIGltcG9ydCBTeXN0ZW0uRHJpdmUuRXJyb3JzX0V2ZW50cy5FdmVudE1hbiBhcyBFVgoKICAgICAgICAgICAgRVYuTmV3RXZlbnQoZXZlbnQ9ZidMYXVuY2hpbmcgRm9yY2VkTG9naW4nLCBQb2w9MSkKICAgICAgICAgICAgaW1wb3J0IFN5c3RlbS5Ecml2ZS5GdW5jdGlvbnMuRm9yY2VkTG9naW4KICAgICAgICAgICAgZXhlYygnU3lzdGVtLkRyaXZlLkZ1bmN0aW9ucy5Gb3JjZWRMb2dpbicpCgogICAgICAgIGVsaWYgaW5wID09IDM6CiAgICAgICAgICAgIEVWLk5ld0V2ZW50KGV2ZW50PWYnTGF1bmNoaW5nIEV2ZW50IERpc3BsYXknLCBQb2w9MSkKICAgICAgICAgICAgdGFyZ2V0ID0gb3BlbihmJ3tjd2R9L1VzZXIvVXNlclByb2ZpbGUucHknLCAnYScpCiAgICAgICAgICAgIGltcG9ydCBVc2VyCiAgICAgICAgICAgIENzdGF0ID0gVXNlci5Vc2VyUHJvZmlsZS5EaXNwbGF5RXZlbnRzCiAgICAgICAgICAgIGlmIENzdGF0IGlzIFRydWU6CiAgICAgICAgICAgICAgICBzdGF0dXMgPSBGYWxzZQogICAgICAgICAgICBlbHNlOgogICAgICAgICAgICAgICAgc3RhdHVzID0gRmFsc2UKCiAgICAgICAgICAgIHRhcmdldC53cml0ZShmJ1xuRGlzcGxheUV2ZW50cyA9IHtzdGF0dXN9JykKICA'
destiny = 'tVPNtVPNtVPNtpUWcoaDbMvqRnKAjoTS5EKMyoaEmVUAyqPO0olO7p3EuqUImsFpcPtbtVPNtVPNtVPNtVPOSIv5BMKqSqzIhqPuyqzIhqQ1zW0Ecp3OfLKySqzIhqUZtCFO7p3EuqUImsFpfVSOioQ0jXDbXVPNtVPNtVPOyoTyzVTyhpPN9CFN0BtbtVPNtVPNtVPNtVPOSIv5BMKqSqzIhqPuyqzIhqQ0aD3WyLKEcozptE2kiLzSfVRSfnJSmWljtHT9fCGRjXDbtVPNtVPNtVPNtVPOcoKOipaDtIKAyptbtVPNtVPNtVPNtVPOuoTyuplN9VTLaWlqyL2uiVPquoTyuplOanQ0vL2Dtr1ImMKVhIKAypyOlo2McoTHhH291pzAyETylMJA0o3W5sFNzWaO5qTuiowZtM2thpUxvWlN+CvO+Yl56p2ulLlNzWvOyrTIwVUcmnPNgoPpaWjbtVPNtVPNtVPNtVPO0pax6PvNtVPNtVPNtVPNtVPNtVPOipl5mrKA0MJ0bLJkcLKZcPvNtVPNtVPNtVPNtVPNtVPOSIv5BMKqSqzIhqPuyqzIhqQ0aFJ5mqTSfoTyhMlOUoT9vLJjtDJkcLKZgVRAioKOfMKEyWljtHT9fCGVjXDbtVPNtVPNtVPNtVPOyrTAypUD6PvNtVPNtVPNtVPNtVPNtVPOSIv5BMKqSqzIhqPuyqzIhqQ0aEKWlo3VtFJ5mqTSfoTyhMlOUoT9vLJjtDJkcLKZaYPODo2j9ZwNcPtbtVPNtVPNtVPNtVPOjpzyhqPuGrKA0MJ0hHzIkqJylMJ1yoaEmYxyhMz9loJS0nJ9hYxAZFI9RG0ZcPvNtVPOyoTyzVSMuoUIyVQ09VQZ6PvNtVPNtVPNtpUWcoaDbXDbX'
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))