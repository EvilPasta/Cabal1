import matplotlib as mpl
import matplotlib.pyplot as plt
import exp

def main():
    owo = exp.Exp()
    # dataPasta = [12038, 16787, 19887, 23899, 27644, 30806, 34400, 37131, 40162, 42771, 44814, 45232, 60384, 66912, 69055, 71238, 73273, 75155, 75655, 76216, 76846, 78608, 78990, 79558, 80412, 81384, 82728, 84152, 86023]
    # 11.21 - 1.22
    dataPasta = [247872990, 248277372, 248802224, 249319703, 249844033, 250283739, 250647959, 251115503, 251584825, 252158429, 252679153, 253278922, 253719681, 254101408, 254624458, 255131278, 255746609, 256368225, 256982857, 257484717, 257907180, 258505285, 259097781, 259755472, 260352979, 260966652, 261452505, 261886641, 262517465, 263117847, 263820271, 264527791, 265258573, 265795368, 266257105, 266854439, 267493525, 268204899, 268903129, 269596747, 270117209, 270576336, 271184033, 271820695, 272560971, 273305012, 274072661, 274645250, 275159510, 275897499, 276656001, 277570594, 278582317, 279473676, 280177765, 280763668, 282037518, 283373894, 285079260, 287029020, 288773032, 290002137, 290932872, 293290670, 295804846, 298389558, 301057654, 304011916, 306202735, 308243739, 311403712, 314434339, 317881431, 321067273, 324384049, 326889149, 329076107, 331721077, 335486018, 339568028, 343297104, 347120112, 349900273, 352365573, 355776286, 359426980, 363186657, 366885827, 370544095, 373287627, 375579743, 379128491]
    Y = owo.CountY(dataPasta, len(dataPasta))
    print("Y: ", Y)
    owo.CheckHyp(len(dataPasta))


    # Output
    listOfX = []
    for i in range(0, len(dataPasta)):
        listOfX.append(i)
    plt.plot(listOfX, dataPasta, label='Infection cases')
    plt.plot(listOfX, Y, label='Exponential function')
    plt.legend(loc='upper left')
    plt.title('Infection cases of Covid-19')
    plt.xlabel('Days')
    plt.ylabel('Cases')
    plt.show()

main()