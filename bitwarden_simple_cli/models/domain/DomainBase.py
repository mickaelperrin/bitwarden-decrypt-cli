import bitwarden_simple_cli.models.domain.CipherString as CipherString


class Domain:

    def __setitem__(self, item, value):
        setattr(self, item, value)

    @staticmethod
    def build_domain_model(domain, data_obj, mapping, already_encrypted, not_enc_list):
        for prop in mapping:
            if prop not in data_obj:
                continue
            obj_prop = data_obj[mapping[prop] or prop]
            if already_encrypted or prop in not_enc_list:
                domain[prop] = obj_prop if obj_prop else None
            else:
                domain[prop] = CipherString.CipherString(obj_prop) if obj_prop else None

    def __getitem__(self, item):
        return getattr(self, item)
