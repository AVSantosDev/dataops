[
  {
    '$lookup': {
      'from': 'montadora', 
      'localField': 'Montadora', 
      'foreignField': 'Montadora', 
      'as': 'Montadoras'
    }
  }, {
    '$project': {
      'Carro': 1, 
      'Cor': 1, 
      'Montadora': 1, 
      'MontadoraInfo': '$Montadoras', 
      'País': '$Montadoras.País'
    }
  }, {
    '$group': {
      '_id': {
        '$first': '$País'
      }, 
      'Carros': {
        '$push': {
          'Carro': '$Carro', 
          'Cor': '$Cor', 
          'Montadora': '$Montadora'
        }
      }
    }
  }
]