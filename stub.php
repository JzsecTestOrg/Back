$testdata = ["ballots"=> [
                "stkcode"=> "600001",
                "stkname"=> "中国",
                "matchdate"=> "20160229",
                "hitqty"=> "676",
                "matchprice"=> "34",
                "hitamt"=> "788.88",
                "payqty"=> "123",
                "payamt"=> "123.09",
                "status"=>"0" ],
			"unpaymt"=> "10000",
			"available_balance"=> "10000"
        ];
        if ("13300000008"==$this->getParam("mobilephone"))
        {
        $this->jsonReturn(0, '中签查询成功', $testdata);
        exit();
        }