import argparse


class EmailGenerator(object):

    def __init__(self):

        parser = argparse.ArgumentParser()
        parser.add_argument('-d', '--domain', dest='domain', action='store', required=True)
        parser.add_argument('-f', '--file', dest='file', action='store', required=True)
        parser.add_argument('-m', '--method', dest='method', default="fn.ln", action='store', required=False)
        parser.add_argument('-o', '--output_file_path', dest='output_file_path', default="emaillistoutput.txt", action='store', required=False)

        try:
            self.__args = parser.parse_args()
        except Exception, err:
            print "Error while parsing arguments"

    def get_email(self, method, name, domain):
        first_name = ""
        last_name = ""
        middle_name = ""
        first_initial = ""
        middle_initial = ""
        last_initial = ""

        #Split name by whitescpaces. This is requred because we need to know if the name contains a middle name.
        name_in_a_list = name.split()

        #if the name length is 2, that means there is no middle name here. Just firstname and lastname
        if len(name_in_a_list) == 2:
            first_name = name_in_a_list[0].lower()
            first_initial = first_name[0]
            last_name = name_in_a_list[1].lower()
            last_initial = last_name[0]
        else:
            first_name = name_in_a_list[0].lower()
            first_initial = first_name[0]
            middle_name = name_in_a_list[1].lower()
            middle_initial = middle_name[0]
            last_name = name_in_a_list[2].lower()
            last_initial = last_name[0]

        #Swtich case for the method string
        switcher = {
            "fn": first_name+'@'+domain,
            "ln": last_name+'@'+domain,
            "fnln": first_name + last_name + '@' + domain,
            "fn.ln": first_name + '.' + last_name + '@' + domain,
            "filn": first_initial + last_name + '@' + domain,
            "fi.ln": first_initial + '.' + last_name + '@' + domain,
            "fnli": first_name + last_initial + '@' + domain,
            "fn.li": first_name + '.' + last_initial + '@' + domain,
            "fili": first_initial + last_initial + '@' + domain,
            "fi.li": first_initial + '.' + last_initial + '@' + domain,
            "lnfn": last_name + first_name + '@' + domain,
            "ln.fn": last_name + '.' + first_name + '@' + domain,
            "lnfi": last_name + first_initial + '@' + domain,
            "ln.fi": last_name + '.' + first_initial + '@' + domain,
            "lifn": last_initial + first_name + '@' + domain,
            "li.fn": last_initial + '.' + first_name + '@' + domain,
            "lifi": last_initial + first_initial + '@' + domain,
            "li.fi": last_initial + '.' + first_initial + '@' + domain,
            "fimiln": first_initial + middle_initial + last_name + '@' + domain,
            "fimi.ln": first_initial + middle_initial + '.' + last_name + '@' + domain,
            "fnmiln": first_name + middle_initial + last_name + '@' + domain,
            "fn.mi.ln": first_name + '.' + middle_initial + '.' + last_name + '@' + domain,
            "fnmnln": first_name + middle_name + last_name + '@' + domain,
            "fn.mn.ln": first_name + '.' + middle_name + '.' + last_name + '@' + domain,
            "fn-ln": first_name + '-' + last_name + '@' + domain,
            "fi-ln": first_initial + '-' + last_name + '@' + domain,
            "fn-li": first_name + '-' + last_initial + '@' + domain,
            "fi-li": first_initial + '-' + last_initial + '@' + domain,
            "ln-fn": last_name + '-' + first_name + '@' + domain,
            "ln-fi": last_name + '-' + first_initial + '@' + domain,
            "li-fn": last_initial + '-' + first_name + '@' + domain,
            "li-fi": last_initial + '-' + first_initial + '@' + domain,
            "fimi-ln": first_initial + middle_initial + '-' + last_name + '@' + domain,
            "fn-mi-ln": first_name + '-' + middle_initial + '-' + last_name + '@' + domain,
            "fn-mn-ln": first_name + '-' + middle_name + '-' + last_name + '@' + domain,
            "fn_ln": first_name + '_' + last_name + '@' + domain,
            "fi_ln": first_initial + '_' + last_name + '@' + domain,
            "fn_li": first_name + '_' + last_initial + '@' + domain,
            "fi_li": first_initial + '_' + last_initial + '@' + domain,
            "ln_fn": last_name + '_' + first_name + '@' + domain,
            "ln_fi": last_name + '_' + first_initial + '@' + domain,
            "li_fn": last_initial + '_' + first_name + '@' + domain,
            "li_fi": last_initial + '_' + first_initial + '@' + domain,
            "fimi_ln": first_initial + middle_initial + '_' + last_name + '@' + domain,
            "fn_mi_ln": first_name + '_' + middle_initial + '_' + last_name + '@' + domain,
            "fn_mn_ln": first_name + '_' + middle_name + '_' + last_name + '@' + domain,
        }
        return switcher.get(method, "first_name + '.' + last_name + '@' + domain")

    def _main(self):

        #Read input file and create a list from the lines
        with open(self.__args.file) as f:
            names = f.readlines()
        #Strip newline chararcters at the end of each line
        names = [name.strip() for name in names]

        #Get the domain from command line arguments
        domain = self.__args.domain

        #Open output file as writable
        output_file = open(self.__args.output_file_path, 'w')

        for name in names:
            method = self.__args.method
            email = self.get_email(method, name, domain)
            output_file.write("%s\n" % email)

        output_file.close()
##
### Main, go go go!
##

if __name__ == "__main__":
    email_generator = EmailGenerator()
    email_generator._main()