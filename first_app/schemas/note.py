
# schemas ki file ka maksad ya ha ka node jo model ma define ki ha us ko kasia ma kam ma laya
def Note_dic(item) -> dict:      # jo model ka andar node banai thi wo node use ho rahi ha
    return {
        "id": item["_id"],
        "title": item["title"],
        "des": item["des"],
        "important":item["important"]
    }
    
def Note_list(items) -> list:
    return[Note_dic(item) for item in items]