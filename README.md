# Stock Portfolio Manager

---

API - Stock Portfolio Manager

---

## Database Relationship Diagram

![Database Relationship Diagram](/documentation/database_relationship_diagram.png/)

---

## Commands

---

***A query for fetching all Instruments:***

```graphql
{
allInstruments{
    name
    symbol
    }
}
```

***A query for fetching a single instrument selectable via id:***

```graphql
query{
    instrument(id:1){
    name
    symbol
    }
}
```

***A query for fetching all Portfolios:***

```graphql
{
allPortfolios{
    name
    description
    holdingValue
    totalProfitLoss
    }
}
```

***A query for fetching a single Portfolio selectable via id:***

```graphql
query{
portfolio(id:1){
    name
    description
    holdingValue
    totalProfitLoss
    }
}
```

***A mutation for creating a Portfolio with fields 'name' and 'description'***

```graphql
mutation firstmutation{
editPortfolio(id:1, name:"test", description:"test"){
portfolio{
    name
    description
  }
}
}
```

***A mutation for editing a Portfolio with fields 'name' and 'description':***

```graphql
mutation firstmutation{
createPortfolio(id:1, name:"new_name", description:"new_name",){
portfolio{
    name
    description
    }
}
}
```

***A mutation for creating a Trade with fields for 'Portfolio', 'Instrument', 'volume' and 'value':***

```graphql
mutation firstmutation{`
createTrade(name:"new_name", symbol:"new_name", description:"new_name", holdingValue:"0", totalProfitLoss:"0", volume:"0", buyValue:"0", sellValue:"0", profitLoss:"0"){
trade{
    name
    symbol
    description
    holdingValue
    totalProfitLoss
    volume
    buyValue
    sellValue
    profitLoss
  }
}
}
```

***A mutation for editing a Trade with fields for 'Portfolio', 'Instrument', 'volume' and 'value':***

```graphql
mutation firstmutation{
createTrade(id:1, name:"new_name", symbol:"new_name", description:"new_name", holdingValue:"0", totalProfitLoss:"0", volume:"0", buyValue:"0", sellValue:"0", profitLoss:"0"){
trade{
    name
    symbol
    description
    holdingValue
    totalProfitLoss
    volume
    buyValue
    sellValue
    profitLoss
    }
}
}
```

---
