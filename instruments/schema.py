import graphene
from graphene_django import DjangoObjectType
from graphene_django import DjangoListField
from .models import Trade


class InstrumentType(DjangoObjectType):
    class Meta:
        model = Trade
        fields = ("iexId", "name", "symbol")


class PortfolioType(DjangoObjectType):
    class Meta:
        model = Trade
        fields = ("name", "description", "holding_value", "total_profit_loss")


class TradeType(DjangoObjectType):
    class Meta:
        model = Trade
        fields = ("name", "symbol", "description", "holding_value", "total_profit_loss", "volume", "buy_value", "sell_value", "profit_loss")


class Query(graphene.ObjectType):

    all_instruments = DjangoListField(InstrumentType)
    all_portfolios = DjangoListField(PortfolioType)
    instrument = graphene.Field(InstrumentType, id=graphene.Int())
    portfolio = graphene.Field(PortfolioType, id=graphene.Int())

    """ A query for fetching all instruments """
    def resolve_all_instruments(root, info):
        return Trade.objects.all()

    """ A query for fetching all portfolios """
    def resolve_all_portfolio(root, info):
        return Trade.objects.all()

    """ A query for fetching all instruments by id """
    def resolve_instrument(root, info, id):
        return Trade.objects.get(pk=id)

    """ A query for fetching all portfolio by id """
    def resolve_portfolio(root, info, id):
        return Trade.objects.get(pk=id)


""" A mutation for creating a Portfolio """


class PortfolioCreateMutation(graphene.Mutation):

    class Arguments:
        name = graphene.String(required=True)
        description = graphene.String(required=True)

    portfolio = graphene.Field(TradeType)

    @classmethod
    def mutate(cls, root, info, name, description):
        portfolio = Trade(name=name, description=description)
        portfolio.save()
        return PortfolioCreateMutation(portfolio=portfolio)


""" A mutation for editing a Portfolio """


class PortfolioEditMutation(graphene.Mutation):

    class Arguments:
        id = graphene.ID()
        name = graphene.String(required=True)
        description = graphene.String(required=True)

    portfolio = graphene.Field(TradeType)

    @classmethod
    def mutate(cls, root, info, id, name, description):
        portfolio = Trade.objects.get(id=id)
        portfolio.name = name
        portfolio.description = description
        portfolio.save()
        return PortfolioEditMutation(portfolio=portfolio)


""" A mutation for creating a Trade """


class TradeCreateMutation(graphene.Mutation):

    class Arguments:
        name = graphene.String(required=True)
        symbol = graphene.String(required=True)
        description = graphene.String(required=True)
        holding_value = graphene.String(required=True)
        total_profit_loss = graphene.String(required=True)
        volume = graphene.String(required=True)
        buy_value = graphene.String(required=True)
        sell_value = graphene.String(required=True)
        profit_loss = graphene.String(required=True)

    trade = graphene.Field(TradeType)

    @classmethod
    def mutate(cls, root, info, name, symbol, description, holding_value, total_profit_loss, volume, buy_value, sell_value, profit_loss):
        trade = Trade(name=name, symbol=symbol, description=description, holding_value=holding_value, total_profit_loss=total_profit_loss, volume=volume, buy_value=buy_value, sell_value=sell_value, profit_loss=profit_loss)
        trade.save()
        return TradeCreateMutation(trade=trade)


""" A mutation for editing a Trade """


class TradeEditMutation(graphene.Mutation):

    class Arguments:
        id = graphene.ID()
        name = graphene.String(required=True)
        symbol = graphene.String(required=True)
        description = graphene.String(required=True)
        holding_value = graphene.String(required=True)
        total_profit_loss = graphene.String(required=True)
        volume = graphene.String(required=True)
        buy_value = graphene.String(required=True)
        sell_value = graphene.String(required=True)
        profit_loss = graphene.String(required=True)

    trade = graphene.Field(TradeType)

    @classmethod
    def mutate(cls, root, info, id, name, symbol, description, holding_value, total_profit_loss, volume, buy_value, sell_value, profit_loss):
        trade = Trade.objects.get(id=id)
        trade.name = name
        trade.symbol = symbol
        trade.description = description
        trade.holding_value = holding_value
        trade.total_profit_loss = total_profit_loss
        trade.volume = volume
        trade.buy_value = buy_value
        trade.sell_value = sell_value
        trade.profit_loss = profit_loss
        trade.save()
        return TradeEditMutation(trade=trade)


class Mutation(graphene.ObjectType):

    create_portfolio = PortfolioCreateMutation.Field()
    edit_portfolio = PortfolioEditMutation.Field()
    create_trade = TradeCreateMutation.Field()
    edit_trade = TradeEditMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
