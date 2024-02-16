import sdk as sdk

s = sdk.Swcapi()


res = s.general.root_get()

if res.any is not None:
    # handle response
    pass