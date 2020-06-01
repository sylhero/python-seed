from fastapi import APIRouter

router = APIRouter()


def test(*args):
    for a in args:
        print(a)


def test2(**args):
    for a in args:
        print(a, args[a])


@router.get("/items/", tags=["items"])
async def read_items():
    test(1, 2, 3, 4, 5, 6)
    test2(test="dfdf", fdfd="dfdfd")
    return [{"itemname": "Foo"}, {"itemname": "Bar"}]


@router.get("/items/{itemname}", tags=["items"])
async def read_item(itemname: str):
    return {"itemname": None}
