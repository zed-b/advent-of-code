import subprocess, unittest, glob, re, os

class TestAllDays(unittest.TestCase):
    def year_test(self, year):
        files = glob.glob("./{}/src/*.py".format(year), recursive=True)
        for file in files:
            sample_in = re.sub(r"/src/", r"/sample_data/", file)
            sample_in = re.sub(r"py$", r"in", sample_in)
            sample_out = re.sub(r"in$", r"out", sample_in)
            if not os.path.isfile(sample_in):
                print("File {} doesn't exist".format(sample_in))
                return False
            if not os.path.isfile(sample_out):
                print("File {} doesn't exist".format(sample_out))
                return False

            cmd = "python3 {} --sample < {}".format(file, sample_in)
            out1 = [l.strip() for l in subprocess.getoutput(cmd).split('\n')]
            with open(sample_out) as f:
                out2 = [l.strip() for l in f.readlines()]
                if out1 != out2:
                    print("In {}:\n{} \ndiffers from:\n{}".format(file, '\n'.join(out1), '\n'.join(out2)))
                    return False
        return True

    def test_2015(self):
        self.assertTrue(self.year_test(2015))

    def test_2020(self):
        self.assertTrue(self.year_test(2020))

unittest.main()