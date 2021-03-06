import json
import datamodel as dt


def is_file(filename):
    try:
        with open(filename):
            return True
    except IOError:
        return False


def dict_to_json(my_dict):
    return json.dumps(my_dict)


def json_to_dict(my_json):
    return json.loads(my_json)


def save_knowledge(knowledge_dict):
    write_to_file('knowledge.txt', dict_to_json(knowledge_dict))


def get_knowledge():
    if is_file('knowledge.txt'):
        return json_to_dict(get_file_contents('knowledge.txt'))
    else:
        print("A NEW DICT WAS GENERATED.")
        feature_dict = dt.new_feature_weights()
        save_knowledge(feature_dict)
        return feature_dict


def write_to_file(filename, data):
    target = open(filename, 'w')
    target.write(str(data))
    target.close
    return True


def get_file_contents(filename):
    txt = open(filename)
    text = txt.read()
    txt.close()
    return text


def testWrite(my_dict):
    assert write_to_file('test.txt', dict_to_json(my_dict))
    print("write test success")


def testRead(filename):
    if is_file(filename):
        assert json_to_dict(get_file_contents(filename))
        print("read test success")

test_dict = {}
test_dict[1] = "test case2"
test_dict[2] = "true"
test_dict[3] = "TEST PASSED"

# testWrite(test_dict)
# testRead('test.txt')
