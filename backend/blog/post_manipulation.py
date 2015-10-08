delimiter = "@@@"

def paragraph_string_to_dict(paragraph):
    ptype, pcontent = paragraph.split(delimiter) #TODO: formating symbol
    return {
        "type": ptype,
        "content": pcontent
    }

def paragraphs_json_to_string(paragraphs):
    result = []
    for paragraph in paragraphs:
        pstring = paragraph['type']
        pstring += delimiter
        pstring += paragraph['content']
        result.append(pstring)
    return "\n\n".join(result)
