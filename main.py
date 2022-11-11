import matplotlib as mpl
import matplotlib.pyplot as plt
import exp
import grad

def main():
    owo = exp.Exp()
    #dataHideri = [3370950, 3449173, 3523204, 3600809, 3680465, 3770907, 3859461, 3949874, 4034115, 4109328, 4185505, 4270891, 4355306, 4450950, 4547281, 4641188, 4719536, 4808676, 4904285, 5009707, 5115662, 5222914, 5327021, 5420228, 5508439, 5600797, 5703352, 5823344, 5944818, 6079862, 6182722, 6283007, 6405752, 6517005, 6655331, 6788893, 6918226, 7029236, 7132289, 7258292, 7395486, 7531678, 7659166, 7793075, 7925019, 8049957, 8193863, 8337068, 8480214, 8661206, 8847077, 8940122, 9082467, 9250645, 9422124, 9601643, 9794139, 9970562, 10139020, 10291742, 10475496, 10690640, 10895640, 11098304, 11288042, 11474321, 11642572, 11852203, 12067468, 12292055, 12525185, 12738051, 12931019, 13125559, 13346622, 13576502, 13821455, 14058797, 14294106, 14505988, 14714176, 14957222, 15232596, 15512280, 15795865, 16045400, 16257212, 16491647, 16755516, 17025804, 17307583, 17595167]
    dataPasta = [25803515, 26085394, 26370828, 26672578, 26946265, 27175247, 27392531, 27639038, 27924338, 28228730, 28545110, 28833797, 29082612, 29349770, 29630318, 29935267, 30250845, 30577478, 30870562, 31125673, 31385603, 31669903, 31981552, 32302474, 32632483, 32918144, 33165126, 33427873, 33710669, 34035191, 34354324, 34683811, 34981111, 35241614, 35552999, 35869068, 36218332, 36577648, 36938056, 37293513, 37582945, 37872987, 38192367, 38573082, 38980028, 39390542, 39762610, 40093810, 40468798, 40857595, 41297092, 41779124, 42273002, 42729255, 43088051, 43571180, 44039553, 44561315, 45112724, 45684473, 46156513, 46595656, 47144100, 47709544, 48201699, 48821016, 49444194, 50043386, 50534230, 51044098, 51615148, 52239938, 52880262, 53541412, 54128224, 54618385, 55144413, 55746620, 56368860, 57022723, 57696959, 58289286, 58787365, 59321709, 59912369, 60529500, 61118623, 61813817, 62421080, 62916556, 63423412]
    Y = owo.CountY(dataPasta, len(dataPasta))
    print("Y: ", Y)
    #owo.CheckHyp(len(dataPasta))
    print('a_id: ', owo.a)
    print('b_id: ', owo.b)
    grad.coefCount(owo.z)

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