def individual_serial(affiliate)->dict:
    return {
        "id":str(affiliate["_id"])
        "name":str(affiliate["name"])
        "email":(affiliate["email"])
    }