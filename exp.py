import scipy as scp
import math

class Exp:
    z = []
    b = 0.0
    a = 0.0

    def log2(self, N):
        return int((math.log(N) / math.log(2)))

    # def getAverage(self, alist):
    #     temp = sum(alist) / len(alist)
    #     return temp

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
            list.append(math.log(e))
        return list

    def CheckHyp(self, t):
        zStar = []
        e = []
        print("b: ", self.b)
        print("a: ", self.a)
        i = 1
        while (i <= t):
            zStar.append(self.b * i + self.a)
            e.append(self.z[i - 1] - zStar[i - 1])
            i += 1
        print("zStar: ", zStar)
        print("e: ", len(e), e)

        eq = []
        for el in e:
            eq.append(math.pow(el, 2))
        eqAvg = sum(eq) / len(eq)
        eAvg = sum(e) / len(e)
        disper = eqAvg - math.pow(eAvg, 2)
        sigma = math.sqrt(disper)

        lg = self.log2(t) + 1
        minList = min(e)
        maxList = max(e)
        deltaList = maxList - minList

        step = deltaList / lg
        intervals = []
        tmpList = minList
        i = 0
        while (i < lg - 1):
            tmpList = tmpList + step
            intervals.append(tmpList)
            i += 1
        print("Intervals - ", intervals)

        obs = []
        i = 0
        while (i <= len(intervals)):
            obs.append(0)
            i += 1

        i = 0
        while (i <= len(e) - 1):
            if (e[i] < intervals[0]):
                obs[0] = obs[0] + 1
            elif (e[i] >= intervals[len(intervals) - 1]):
                obs[len(obs) - 1] = obs[len(obs) - 1] + 1
            else:
                j = 1
                while (j < len(intervals)):
                    if (e[i] < intervals[j]):
                        obs[j] = obs[j] + 1
                        break
                    j += 1
            i += 1

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

        i = 1
        while (i < len(intervals)):
            P.append(self.FI(intervals[i] / sigma) - self.FI(intervals[i-1] / sigma))
            i += 1
        P.append(0.5 - self.FI(intervals[len(intervals)-1]/sigma))
        print("P: ", P)
        Psum = 0.0
        i = 0
        while (i < len(P)):
            Psum += P[i]
            i += 1
        print("Psum: ", Psum)

        nSt = []
        for el in P:
            nSt.append(t * el)

        print("nSt: ", nSt)
        nStsum = 0.0
        i = 0
        while (i < len(nSt)):
            nStsum += nSt[i]
            i += 1
        print("nStsum: ", nStsum)

        # sumobs = sum(obs)
        # delta = sumobs - nStsum
        # if (delta > 0):
        #     nSt[nSt.index(min(nSt))] += delta
        # else:
        #     nSt[nSt.index(max(nSt))] -= delta

        K, p = scp.stats.chisquare(obs, nSt, ddof=1)
        print("K =", K, "; p =", p)

        if (p <= 0.05):
            print("p <= 0.05. Критерий не верен!")
        else:
            print("p > 0.05. Гипотеза верна!")



    def CountY(self, data, t):
        self.z = self.lnArr(data)
        print("Z: ", self.z)

        zAvg = sum(self.z) / len(self.z)


        tSum = float((int((t * (t + 1)) / 2)))
        tAvg = tSum / t


        zt = []
        tq = []
        i = 1
        while (i <= t):
            zt.append(self.z[i - 1] * i)
            tq.append(math.pow(i, 2))
            i += 1

        ztAvg = sum(zt) / len(zt)
        tqAvg = sum(tq) / len(tq)
        print("zAvg: ", zAvg)
        print("ztAvg: ", ztAvg)
        print("tqAvg: ", tqAvg)
        print("tAvg: ", tAvg)
        self.b = (ztAvg - (zAvg * tAvg)) / (tqAvg - math.pow(tAvg, 2))
        self.a = (zAvg - (self.b * tAvg))
        A = math.exp(self.a)

        yList = []
        i = 1
        while (i <= t):
            yList.append(A * math.exp(self.b * i))
            i += 1

        return yList
