#print the retrieved tweets to the screen:
senators=[	
		{"name": "Luther Strange", "twitter_handle": "SenatorStrange", "state": "Alabama", "party": "R"},
		{"name": "Richard Shelby", "twitter_handle": "SenShelby", "state": "Alabama", "party": "R"},
		{"name": "Dan Sullivan", "twitter_handle": "SenDanSullivan", "state": "Alaska", "party": "R"},
		{"name": "Lisa Murkowski", "twitter_handle": "lisamurkowski", "state": "Alaska", "party": "R"},
		{"name": "John McCain", "twitter_handle": "SenJohnMcCain", "state": "Arizona", "party": "R"},
		{"name": "Jeff Flake", "twitter_handle": "JeffFlake", "state": "Arizona", "party": "R"},
		{"name": "Tom Cotton", "twitter_handle": "SenTomCotton", "state": "Arkansas", "party": "R"},
		{"name": "John Boozman", "twitter_handle": "JohnBoozman", "state": "Arkansas", "party": "R"},
		{"name": "Dianne Feinstein", "twitter_handle": "SenFeinstein", "state": "California", "party": "D"},
		{"name": "Kamala Harris", "twitter_handle": "KamalaHarris", "state": "California", "party": "D"},
		{"name": "Cory Gardner", "twitter_handle": "SenCoryGardner", "state": "Colorado", "party": "R"},
		{"name": "Michael Bennet", "twitter_handle": "SenBennetCO", "state": "Colorado", "party": "D"},
		{"name": "Richard Blumenthal", "twitter_handle": "SenBlumenthal", "state": "Connecticut", "party": "D"},
		{"name": "Chris Murphy", "twitter_handle": "ChrisMurphyCT", "state": "Connecticut", "party": "D"},
		{"name": "Tom Carper", "twitter_handle": "SenatorCarper", "state": "Delaware", "party": "D"},
		{"name": "Chris Coons", "twitter_handle": "ChrisCoons", "state": "Delaware", "party": "D"},
		{"name": "Bill Nelson", "twitter_handle": "SenBillNelson", "state": "Florida", "party": "D"},
		{"name": "Marco Rubio", "twitter_handle": "marcorubio", "state": "Florida", "party": "R"},
		{"name": "David Perdue", "twitter_handle": "sendavidperdue", "state": "Georgia", "party": "R"},
		{"name": "Johnny Isakson", "twitter_handle": "SenatorIsakson", "state": "Georgia", "party": "R"},
		{"name": "Brian Schatz", "twitter_handle": "SenBrianSchatz", "state": "Hawaii", "party": "D"},
		{"name": "Mazie Hirono", "twitter_handle": "maziehirono", "state": "Hawaii", "party": "D"},
		{"name": "Jim Risch", "twitter_handle": "SenatorRisch", "state": "Idaho", "party": "R"},
		{"name": "Mike Crapo", "twitter_handle": "MikeCrapo", "state": "Idaho", "party": "R"},
		{"name": "Tammy Duckworth", "twitter_handle": "senjohnbarrasso", "state": "Illinois", "party": "D"},
		{"name": "Dick Durbin", "twitter_handle": "SenatorDurbin", "state": "Illinois", "party": "D"},
		{"name": "Todd Young", "twitter_handle": "SenToddYoung", "state": "Indiana", "party": "R"},
		{"name": "Joe Donnelly", "twitter_handle": "SenDonnelly", "state": "Indiana", "party": "D"},
		{"name": "Joni Ernst", "twitter_handle": "SenJoniErnst", "state": "Iowa", "party": "R"},
		{"name": "Chuck Grassley", "twitter_handle": "ChuckGrassley", "state": "Iowa", "party": "R"},
		{"name": "Pat Roberts", "twitter_handle": "SenPatRoberts", "state": "Kansas", "party": "R"},
		{"name": "Jerry Moran", "twitter_handle": "JerryMoran", "state": "Kansas", "party": "R"},
		{"name": "Mitch McConnell", "twitter_handle": "SenateMajLdr", "state": "Kentucky", "party": "R"},
		{"name": "Rand Paul", "twitter_handle": "RandPaul", "state": "Kentucky", "party": "R"},
		{"name": "John Kennedy", "twitter_handle": "SenJohnKennedy", "state": "Louisiana", "party": "R"},
		{"name": "Bill Cassidy", "twitter_handle": "BillCassidy", "state": "Louisiana", "party": "R"},
		{"name": "Angus King", "twitter_handle": "SenAngusKing", "state": "Maine", "party": "I"},
		{"name": "Susan Collins", "twitter_handle": "SenatorCollins", "state": "Maine", "party": "R"},
		{"name": "Ben Cardin", "twitter_handle": "SenatorCardin", "state": "Maryland", "party": "D"},
		{"name": "Chris Van Hollen", "twitter_handle": "ChrisVanHollen", "state": "Maryland", "party": "D"},
		{"name": "Elizabeth Warren", "twitter_handle": "SenWarren", "state": "Massachusetts", "party": "D"},
		{"name": "Ed Markey", "twitter_handle": "SenMarkey", "state": "Massachusetts", "party": "D"},
		{"name": "Gary Peters", "twitter_handle": "SenGaryPeters", "state": "Michigan", "party": "D"},
		{"name": "Debbie Stabenow", "twitter_handle": "SenStabenow", "state": "Michigan", "party": "D"},
		{"name": "Amy Klobuchar", "twitter_handle": "amyklobuchar", "state": "Minnesota", "party": "D"},
		{"name": "Al Franken", "twitter_handle": "alfranken", "state": "Minnesota", "party": "D"},
		{"name": "Thad Cochran", "twitter_handle": "SenThadCochran", "state": "Mississippi", "party": "R"},
		{"name": "Roger Wicker", "twitter_handle": "SenatorWicker", "state": "Mississippi", "party": "R"},
		{"name": "Roy Blunt", "twitter_handle": "RoyBlunt", "state": "Missouri", "party": "R"},
		{"name": "Claire McCaskill", "twitter_handle": "clairecmc", "state": "Missouri", "party": "D"},
		{"name": "Jon Tester", "twitter_handle": "SenatorTester", "state": "Montana", "party": "D"},
		{"name": "Steve Daines", "twitter_handle": "SteveDaines", "state": "Montana", "party": "R"},
		{"name": "Ben Sasse", "twitter_handle": "SenSasse", "state": "Nebraska", "party": "R"},
		{"name": "Deb Fischer", "twitter_handle": "SenatorFischer", "state": "Nebraska", "party": "R"},
		{"name": "Cortez Masto", "twitter_handle": "SenCortezMasto", "state": "Nevada", "party": "D"},
		{"name": "Dean Heller", "twitter_handle": "SenDeanHeller", "state": "Nevada", "party": "R"},
		{"name": "Maggie Hassan", "twitter_handle": "SenatorHassan", "state": "New Hampshire", "party": "D"},
		{"name": "Jeanne Shaheen", "twitter_handle": "SenatorShaheen", "state": "New Hampshire", "party": "D"},
		{"name": "Bob Menendez", "twitter_handle": "SenatorMenendez", "state": "New Jersey", "party": "D"},
		{"name": "Cory Booker", "twitter_handle": "CoryBooker", "state": "New Jersey", "party": "D"},
		{"name": "Martin Heinrich", "twitter_handle": "MartinHeinrich", "state": "New Mexico", "party": "D"},
		{"name": "Tom Udall", "twitter_handle": "SenatorTomUdall", "state": "New Mexico", "party": "D"},
		{"name": "Kirsten Gillibrand", "twitter_handle": "SenGillibrand", "state": "New York", "party": "D"},
		{"name": "Chuck Schumer", "twitter_handle": "SenSchumer", "state": "New York", "party": "D"},
		{"name": "Thom Tillis", "twitter_handle": "SenThomTillis", "state": "North Carolina", "party": "R"},
		{"name": "Richard Burr", "twitter_handle": "SenatorBurr", "state": "North Carolina", "party": "R"},
		{"name": "Heidi Heitkamp", "twitter_handle": "SenatorHeitkamp", "state": "North Dakota", "party": "D"},
		{"name": "John Hoeven", "twitter_handle": "SenJohnHoeven", "state": "North Dakota", "party": "D"},
		{"name": "Sherrod Brown", "twitter_handle": "SenSherrodBrown", "state": "Ohio", "party": "D"},
		{"name": "Rob Portman", "twitter_handle": "senrobportman", "state": "Ohio", "party": "R"},
		{"name": "James Lankford", "twitter_handle": "SenatorLankford", "state": "Oklahoma", "party": "R"},
		{"name": "Jim Inhofe", "twitter_handle": "jiminhofe", "state": "Oklahoma", "party": "R"},
		{"name": "Ron Wyden", "twitter_handle": "RonWyden", "state": "Oregon", "party": "D"},
		{"name": "Jeff Merkley", "twitter_handle": "SenJeffMerkley", "state": "Oregon", "party": "D"},
		{"name": "Pat Toomey", "twitter_handle": "SenToomey", "state": "Pennsylvania", "party": "R"},
		{"name": "Bob Casey", "twitter_handle": "SenBobCasey", "state": "Pennsylvania", "party": "D"},
		{"name": "Jack Reed", "twitter_handle": "SenJackReed", "state": "Rhode Island", "party": "D"},
		{"name": "Sheldon Whitehouse", "twitter_handle": "SenWhitehouse", "state": "Rhode Island", "party": "D"},
		{"name": "Tim Scott", "twitter_handle": "SenatorTimScott", "state": "South Carolina", "party": "R"},
		{"name": "Lindsey Graham", "twitter_handle": "GrahamBlog", "state": "South Carolina", "party": "R"},
		{"name": "Mike Rounds", "twitter_handle": "SenatorRounds", "state": "South Dakota", "party": "R"},
		{"name": "John Thune", "twitter_handle": "SenJohnThune", "state": "South Dakota", "party": "R"},
		{"name": "Lamar Alexander", "twitter_handle": "SenAlexander", "state": "Tennessee", "party": "R"},
		{"name": "Bob Corker", "twitter_handle": "SenBobCorker", "state": "Tennessee", "party": "R"},
		{"name": "Ted Cruz", "twitter_handle": "SenTedCruz", "state": "Texas", "party": "R"},
		{"name": "John Cornyn", "twitter_handle": "JohnCornyn", "state": "Texas", "party": "R"},
		{"name": "Orrin Hatch", "twitter_handle": "SenOrrinHatch", "state": "Utah", "party": "R"},
		{"name": "Mike Lee", "twitter_handle": "SenMikeLee", "state": "Utah", "party": "R"},
		{"name": "Patrick Leahy", "twitter_handle": "SenatorLeahy", "state": "Vermont", "party": "D"},
		{"name": "Bernie Sanders", "twitter_handle": "SenSanders", "state": "Vermont", "party": "I"},
		{"name": "Tim Kaine", "twitter_handle": "timkaine", "state": "Virginia", "party": "D"},
		{"name": "Mark Warner", "twitter_handle": "MarkWarner", "state": "Virginia", "party": "D"},
		{"name": "Patty Murray", "twitter_handle": "PattyMurray", "state": "Washington", "party": "D"},
		{"name": "Maria Cantwell", "twitter_handle": "SenatorCantwell", "state": "Washington", "party": "D"},
		{"name": "Joe Manchin", "twitter_handle": "Sen_JoeManchin", "state": "West Virginia", "party": "D"},
		{"name": "Shelley Moore Capito", "twitter_handle": "SenCapito", "state": "West Virginia", "party": "R"},
		{"name": "Tammy Baldwin", "twitter_handle": "SenatorBaldwin", "state": "Wisconsin", "party": "D"},
		{"name": "Ron Johnson", "twitter_handle": "SenRonJohnson", "state": "Wisconsin", "party": "R"},
		{"name": "Mike Enzi", "twitter_handle": "SenatorEnzi", "state": "Wyoming", "party": "R"},
		{"name": "John Barraso", "twitter_handle": "senjohnbarrasso", "state": "Wyoming", "party": "R"}] 
