def get_model(model_name, args):
    name = model_name.lower()
    if name == "wa":
        from models.wa import WA
        return WA(args)
    else:
        assert 0
