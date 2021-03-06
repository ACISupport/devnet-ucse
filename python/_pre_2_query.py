# Currently UCSM SDK does not work with Python 3.9 as of this writing - 12/13/20

from ucsmsdk.ucshandle import UcsHandle

def main():
    handle = UcsHandle("10.0.0.201","ucspe","ucspe", secure=False)
    handle.login()
    
    ## Query Based on Class Name
    print("\n\n=== Query Based on Class Name")
    blades = handle.query_classid("computeBlade")
    for blade in blades:
        print(blade.dn,blade.name,blade.model)
    
    ## Query Class Name with filter
    print("\n\n=== Query Based on Class Name with Filter equal to")
    filter = "(model, 'UCSB-EX-M4-1', type='eq')"
    blades = handle.query_classid("computeBlade",filter_str=filter)
    for blade in blades:
        print(blade.dn,blade.name,blade.model)
    
    print("\n\n=== Query Based on Class Name with Filter not-equal to")
    filter = "(model,'UCSB-EX-M4-1',type='ne')"
    blades = handle.query_classid("computeBlade",filter_str=filter)
    for blade in blades:
        print(blade.dn,blade.name,blade.model)

    ## Query Directly the DN of an Object
    print("\n\n=== Query Based on Distinguished Name")
    blade = handle.query_dn(blades[0].dn)
    print(blade)

    handle.logout()

if __name__ == "__main__":
    main()
