import scipy as scp
import numpy as np

class Exp:
    z = []
    b = 0.0
    a = 0.0

    def FI(self, x):
        return scp.stats.norm.cdf(x) - 0.5

    def checkGreaterThan(self, list, number):
        for el in list:
            if (el < number):
                return False
        return True

    def lnArr(self, arr):
        list = []
        for e in arr:
            list.append(np.log(e))
        return list

    def CheckHyp(self, t):
        zStar = []
        e = []
        print("b: ", self.b)
        print("a: ", self.a)
        for i in range(1, t+1):
            zStar.append(self.b * i + self.a)
            e.append(self.z[i-1] - zStar[i-1])
        print("zStar: ", zStar)
        print("e: ", len(e), e)

        eq = []
        for el in e:
            eq.append(pow(el, 2))
        eqAvg = np.average(eq)
        eAvg = np.average(e)
        disper = eqAvg - pow(eAvg, 2)
        sigma = np.sqrt(disper)

        lg = int(np.trunc(np.log2(t)))
        minList = min(e)
        maxList = max(e)
        deltaList = maxList - minList

        step = deltaList / lg
        intervals = []
        tmpList = minList
        for i in range(0, lg):
            tmpList = tmpList + step
            intervals.append(tmpList)
        print("Intervals - ", intervals)

        obs = []
        for i in range(0, len(intervals) + 1):
            obs.append(0)

        for i in range(len(e)):
            if (e[i] < intervals[0]):
                obs[0] = obs[0] + 1
            elif (e[i] >= intervals[len(intervals) - 1]):
                obs[len(obs) - 1] = obs[len(obs) - 1] + 1
            else:
                for j in range(1, len(intervals)):
                    if (e[i] < intervals[j]):
                        obs[j] = obs[j] + 1
                        break

        print("OBS: ", obs)

        while (not self.checkGreaterThan(obs, 5) and len(obs) > 2):
            i = 0
            while (i < len(obs)):
                if (obs[i] < 5):
                    if (i != len(obs) - 1):
                        obs[i+1] = obs[i+1] + obs[i]
                    else:
                        obs[i-1] = obs[i-1] + obs[i]
                    if (len(obs) > 1):
                        obs.pop(i)
                        if (i >= len(intervals)):
                            intervals.pop(i-1)
                        else:
                            intervals.pop(i)
                    else:
                        break
                else:
                    i += 1

        print("OBS Valid: ", obs)
        print("Intervals Valid", intervals)

        P = []

        P.append(self.FI(intervals[0] / sigma) + 0.5)
        for i in range(1, len(intervals)):
            P.append(self.FI(intervals[i] / sigma) - self.FI(intervals[i-1] / sigma))
        P.append(0.5 - self.FI(intervals[len(intervals)-1]) / sigma)
        print("P: ", P)
        Psum = 0.0
        for i in range(0, len(P)):
            Psum += P[i]
        print("Psum: ", Psum)

        nSt = []
        for el in P:
            nSt.append(t * el)
        print("nSt: ", nSt)
        nStsum = 0.0
        for i in range(len(nSt)):
            nStsum += nSt[i]
        print("nStsum: ", nStsum)

        K, p = scp.stats.chisquare(obs, nSt, ddof=1)
        print("K = ", K, "; p = ", p)



    def CountY(self, data, t):
        self.z = self.lnArr(data)
        print("Z: ", self.z)

        zAvg = np.average(self.z)


        tSum = (t * (t + 1)) / 2
        tAvg = tSum / t


        zt = []
        tq = []
        for i in range(1, t+1):
            zt.append(self.z[i - 1] * i)
            tq.append(pow(i, 2))

        ztAvg = np.average(zt)
        tqAvg = np.average(tq)
        print("zAvg: ", zAvg)
        print("ztAvg: ", ztAvg)
        print("tqAvg: ", tqAvg)
        print("tAvg: ", tAvg)
        self.b = (ztAvg - (zAvg * tAvg)) / (tqAvg - pow(tAvg, 2))
        print("Chis: ", (ztAvg - (zAvg * tAvg)))
        print("Znam: ", (tqAvg - pow(tAvg, 2)))
        self.a = (zAvg - (self.b * tAvg))
        A = pow(np.e, self.a)

        yList = []
        for i in range(1, t+1):
            yList.append(A * pow(np.e, self.b*i))

        return yList
