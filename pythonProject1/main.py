let rec chanceFor123 (k:int) =
    let gll = new Random()
    let rec chance i suma =
        if i = k then
            (float)suma/(float)k
        else
            let (throw1, throw2, throw3) = (gll.Next(6) + 1, gll.Next(6) + 1, gll.Next(6) + 1)
            if (throw1 = 1 && throw2 = 2 && throw3 = 3)
                || (throw1 = 1 && throw2 = 3 && throw3 = 2)
                || (throw1 = 2 && throw2 = 1 && throw3 = 3)
                || (throw1 = 2 && throw2 = 3 && throw3 = 1)
                || (throw1 = 3 && throw2 = 2 && throw3 = 1)
                || (throw1 = 3 && throw2 = 1 && throw3 = 2)
            then
                chance (i + 1) (suma + 1)
            else
                chance (i + 1) suma
    chance 0 0