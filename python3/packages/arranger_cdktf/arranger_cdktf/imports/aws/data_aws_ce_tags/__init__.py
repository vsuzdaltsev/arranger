'''
# `data_aws_ce_tags`

Refer to the Terraform Registory for docs: [`data_aws_ce_tags`](https://www.terraform.io/docs/providers/aws/d/ce_tags).
'''
import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from typeguard import check_type

from .._jsii import *

import cdktf as _cdktf_9a9027ec
import constructs as _constructs_77d1e7e8


class DataAwsCeTags(
    _cdktf_9a9027ec.TerraformDataSource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.dataAwsCeTags.DataAwsCeTags",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/d/ce_tags aws_ce_tags}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        time_period: typing.Union["DataAwsCeTagsTimePeriod", typing.Dict[builtins.str, typing.Any]],
        filter: typing.Optional[typing.Union["DataAwsCeTagsFilter", typing.Dict[builtins.str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        search_string: typing.Optional[builtins.str] = None,
        sort_by: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataAwsCeTagsSortBy", typing.Dict[builtins.str, typing.Any]]]]] = None,
        tag_key: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/d/ce_tags aws_ce_tags} Data Source.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param time_period: time_period block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#time_period DataAwsCeTags#time_period}
        :param filter: filter block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#filter DataAwsCeTags#filter}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#id DataAwsCeTags#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param search_string: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#search_string DataAwsCeTags#search_string}.
        :param sort_by: sort_by block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#sort_by DataAwsCeTags#sort_by}
        :param tag_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#tag_key DataAwsCeTags#tag_key}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__667a4290670c8642e77287d6f96f41ff5782a1fcc3790536d05070713877dcad)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = DataAwsCeTagsConfig(
            time_period=time_period,
            filter=filter,
            id=id,
            search_string=search_string,
            sort_by=sort_by,
            tag_key=tag_key,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putFilter")
    def put_filter(
        self,
        *,
        and_: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataAwsCeTagsFilterAnd", typing.Dict[builtins.str, typing.Any]]]]] = None,
        cost_category: typing.Optional[typing.Union["DataAwsCeTagsFilterCostCategory", typing.Dict[builtins.str, typing.Any]]] = None,
        dimension: typing.Optional[typing.Union["DataAwsCeTagsFilterDimension", typing.Dict[builtins.str, typing.Any]]] = None,
        not_: typing.Optional[typing.Union["DataAwsCeTagsFilterNot", typing.Dict[builtins.str, typing.Any]]] = None,
        or_: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataAwsCeTagsFilterOr", typing.Dict[builtins.str, typing.Any]]]]] = None,
        tags: typing.Optional[typing.Union["DataAwsCeTagsFilterTags", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param and_: and block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#and DataAwsCeTags#and}
        :param cost_category: cost_category block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#cost_category DataAwsCeTags#cost_category}
        :param dimension: dimension block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#dimension DataAwsCeTags#dimension}
        :param not_: not block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#not DataAwsCeTags#not}
        :param or_: or block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#or DataAwsCeTags#or}
        :param tags: tags block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#tags DataAwsCeTags#tags}
        '''
        value = DataAwsCeTagsFilter(
            and_=and_,
            cost_category=cost_category,
            dimension=dimension,
            not_=not_,
            or_=or_,
            tags=tags,
        )

        return typing.cast(None, jsii.invoke(self, "putFilter", [value]))

    @jsii.member(jsii_name="putSortBy")
    def put_sort_by(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataAwsCeTagsSortBy", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__47fc611d46d4baa1fcab8358f9444bbe04ca61efc2e7e09fa0b41b929301f809)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putSortBy", [value]))

    @jsii.member(jsii_name="putTimePeriod")
    def put_time_period(self, *, end: builtins.str, start: builtins.str) -> None:
        '''
        :param end: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#end DataAwsCeTags#end}.
        :param start: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#start DataAwsCeTags#start}.
        '''
        value = DataAwsCeTagsTimePeriod(end=end, start=start)

        return typing.cast(None, jsii.invoke(self, "putTimePeriod", [value]))

    @jsii.member(jsii_name="resetFilter")
    def reset_filter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFilter", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetSearchString")
    def reset_search_string(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSearchString", []))

    @jsii.member(jsii_name="resetSortBy")
    def reset_sort_by(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSortBy", []))

    @jsii.member(jsii_name="resetTagKey")
    def reset_tag_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagKey", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="filter")
    def filter(self) -> "DataAwsCeTagsFilterOutputReference":
        return typing.cast("DataAwsCeTagsFilterOutputReference", jsii.get(self, "filter"))

    @builtins.property
    @jsii.member(jsii_name="sortBy")
    def sort_by(self) -> "DataAwsCeTagsSortByList":
        return typing.cast("DataAwsCeTagsSortByList", jsii.get(self, "sortBy"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="timePeriod")
    def time_period(self) -> "DataAwsCeTagsTimePeriodOutputReference":
        return typing.cast("DataAwsCeTagsTimePeriodOutputReference", jsii.get(self, "timePeriod"))

    @builtins.property
    @jsii.member(jsii_name="filterInput")
    def filter_input(self) -> typing.Optional["DataAwsCeTagsFilter"]:
        return typing.cast(typing.Optional["DataAwsCeTagsFilter"], jsii.get(self, "filterInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="searchStringInput")
    def search_string_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "searchStringInput"))

    @builtins.property
    @jsii.member(jsii_name="sortByInput")
    def sort_by_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAwsCeTagsSortBy"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAwsCeTagsSortBy"]]], jsii.get(self, "sortByInput"))

    @builtins.property
    @jsii.member(jsii_name="tagKeyInput")
    def tag_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tagKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="timePeriodInput")
    def time_period_input(self) -> typing.Optional["DataAwsCeTagsTimePeriod"]:
        return typing.cast(typing.Optional["DataAwsCeTagsTimePeriod"], jsii.get(self, "timePeriodInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__021a152aa25ff3db1bc9655df6bf81b235d0fe675e2ff4fa65805c5bc8f6daea)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="searchString")
    def search_string(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "searchString"))

    @search_string.setter
    def search_string(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__044656f1cee5cbdbcb3cbd49c8a917b9feb84a776ff81dfb554c95bbeb184440)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "searchString", value)

    @builtins.property
    @jsii.member(jsii_name="tagKey")
    def tag_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tagKey"))

    @tag_key.setter
    def tag_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8d2a655c3fa75a1984ff8549b1f677016cf3e554f5eb5894835c184e8eb31f44)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagKey", value)


@jsii.data_type(
    jsii_type="aws.dataAwsCeTags.DataAwsCeTagsConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "time_period": "timePeriod",
        "filter": "filter",
        "id": "id",
        "search_string": "searchString",
        "sort_by": "sortBy",
        "tag_key": "tagKey",
    },
)
class DataAwsCeTagsConfig(_cdktf_9a9027ec.TerraformMetaArguments):
    def __init__(
        self,
        *,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
        time_period: typing.Union["DataAwsCeTagsTimePeriod", typing.Dict[builtins.str, typing.Any]],
        filter: typing.Optional[typing.Union["DataAwsCeTagsFilter", typing.Dict[builtins.str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        search_string: typing.Optional[builtins.str] = None,
        sort_by: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataAwsCeTagsSortBy", typing.Dict[builtins.str, typing.Any]]]]] = None,
        tag_key: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param time_period: time_period block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#time_period DataAwsCeTags#time_period}
        :param filter: filter block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#filter DataAwsCeTags#filter}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#id DataAwsCeTags#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param search_string: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#search_string DataAwsCeTags#search_string}.
        :param sort_by: sort_by block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#sort_by DataAwsCeTags#sort_by}
        :param tag_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#tag_key DataAwsCeTags#tag_key}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(time_period, dict):
            time_period = DataAwsCeTagsTimePeriod(**time_period)
        if isinstance(filter, dict):
            filter = DataAwsCeTagsFilter(**filter)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e5bd96f2a3880010cc9f0d34c2fe1c2375a3b7c96a10ca408423c9e990d01c44)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument time_period", value=time_period, expected_type=type_hints["time_period"])
            check_type(argname="argument filter", value=filter, expected_type=type_hints["filter"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument search_string", value=search_string, expected_type=type_hints["search_string"])
            check_type(argname="argument sort_by", value=sort_by, expected_type=type_hints["sort_by"])
            check_type(argname="argument tag_key", value=tag_key, expected_type=type_hints["tag_key"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "time_period": time_period,
        }
        if connection is not None:
            self._values["connection"] = connection
        if count is not None:
            self._values["count"] = count
        if depends_on is not None:
            self._values["depends_on"] = depends_on
        if for_each is not None:
            self._values["for_each"] = for_each
        if lifecycle is not None:
            self._values["lifecycle"] = lifecycle
        if provider is not None:
            self._values["provider"] = provider
        if provisioners is not None:
            self._values["provisioners"] = provisioners
        if filter is not None:
            self._values["filter"] = filter
        if id is not None:
            self._values["id"] = id
        if search_string is not None:
            self._values["search_string"] = search_string
        if sort_by is not None:
            self._values["sort_by"] = sort_by
        if tag_key is not None:
            self._values["tag_key"] = tag_key

    @builtins.property
    def connection(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, _cdktf_9a9027ec.WinrmProvisionerConnection]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("connection")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, _cdktf_9a9027ec.WinrmProvisionerConnection]], result)

    @builtins.property
    def count(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def depends_on(
        self,
    ) -> typing.Optional[typing.List[_cdktf_9a9027ec.ITerraformDependable]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("depends_on")
        return typing.cast(typing.Optional[typing.List[_cdktf_9a9027ec.ITerraformDependable]], result)

    @builtins.property
    def for_each(self) -> typing.Optional[_cdktf_9a9027ec.ITerraformIterator]:
        '''
        :stability: experimental
        '''
        result = self._values.get("for_each")
        return typing.cast(typing.Optional[_cdktf_9a9027ec.ITerraformIterator], result)

    @builtins.property
    def lifecycle(self) -> typing.Optional[_cdktf_9a9027ec.TerraformResourceLifecycle]:
        '''
        :stability: experimental
        '''
        result = self._values.get("lifecycle")
        return typing.cast(typing.Optional[_cdktf_9a9027ec.TerraformResourceLifecycle], result)

    @builtins.property
    def provider(self) -> typing.Optional[_cdktf_9a9027ec.TerraformProvider]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provider")
        return typing.cast(typing.Optional[_cdktf_9a9027ec.TerraformProvider], result)

    @builtins.property
    def provisioners(
        self,
    ) -> typing.Optional[typing.List[typing.Union[_cdktf_9a9027ec.FileProvisioner, _cdktf_9a9027ec.LocalExecProvisioner, _cdktf_9a9027ec.RemoteExecProvisioner]]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provisioners")
        return typing.cast(typing.Optional[typing.List[typing.Union[_cdktf_9a9027ec.FileProvisioner, _cdktf_9a9027ec.LocalExecProvisioner, _cdktf_9a9027ec.RemoteExecProvisioner]]], result)

    @builtins.property
    def time_period(self) -> "DataAwsCeTagsTimePeriod":
        '''time_period block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#time_period DataAwsCeTags#time_period}
        '''
        result = self._values.get("time_period")
        assert result is not None, "Required property 'time_period' is missing"
        return typing.cast("DataAwsCeTagsTimePeriod", result)

    @builtins.property
    def filter(self) -> typing.Optional["DataAwsCeTagsFilter"]:
        '''filter block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#filter DataAwsCeTags#filter}
        '''
        result = self._values.get("filter")
        return typing.cast(typing.Optional["DataAwsCeTagsFilter"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#id DataAwsCeTags#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def search_string(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#search_string DataAwsCeTags#search_string}.'''
        result = self._values.get("search_string")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sort_by(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAwsCeTagsSortBy"]]]:
        '''sort_by block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#sort_by DataAwsCeTags#sort_by}
        '''
        result = self._values.get("sort_by")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAwsCeTagsSortBy"]]], result)

    @builtins.property
    def tag_key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#tag_key DataAwsCeTags#tag_key}.'''
        result = self._values.get("tag_key")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAwsCeTagsConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.dataAwsCeTags.DataAwsCeTagsFilter",
    jsii_struct_bases=[],
    name_mapping={
        "and_": "and",
        "cost_category": "costCategory",
        "dimension": "dimension",
        "not_": "not",
        "or_": "or",
        "tags": "tags",
    },
)
class DataAwsCeTagsFilter:
    def __init__(
        self,
        *,
        and_: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataAwsCeTagsFilterAnd", typing.Dict[builtins.str, typing.Any]]]]] = None,
        cost_category: typing.Optional[typing.Union["DataAwsCeTagsFilterCostCategory", typing.Dict[builtins.str, typing.Any]]] = None,
        dimension: typing.Optional[typing.Union["DataAwsCeTagsFilterDimension", typing.Dict[builtins.str, typing.Any]]] = None,
        not_: typing.Optional[typing.Union["DataAwsCeTagsFilterNot", typing.Dict[builtins.str, typing.Any]]] = None,
        or_: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataAwsCeTagsFilterOr", typing.Dict[builtins.str, typing.Any]]]]] = None,
        tags: typing.Optional[typing.Union["DataAwsCeTagsFilterTags", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param and_: and block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#and DataAwsCeTags#and}
        :param cost_category: cost_category block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#cost_category DataAwsCeTags#cost_category}
        :param dimension: dimension block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#dimension DataAwsCeTags#dimension}
        :param not_: not block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#not DataAwsCeTags#not}
        :param or_: or block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#or DataAwsCeTags#or}
        :param tags: tags block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#tags DataAwsCeTags#tags}
        '''
        if isinstance(cost_category, dict):
            cost_category = DataAwsCeTagsFilterCostCategory(**cost_category)
        if isinstance(dimension, dict):
            dimension = DataAwsCeTagsFilterDimension(**dimension)
        if isinstance(not_, dict):
            not_ = DataAwsCeTagsFilterNot(**not_)
        if isinstance(tags, dict):
            tags = DataAwsCeTagsFilterTags(**tags)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0c166be0dbd327fcbc6f1bd0288e92351a4a7e955fd05982f2a40880d4d758a2)
            check_type(argname="argument and_", value=and_, expected_type=type_hints["and_"])
            check_type(argname="argument cost_category", value=cost_category, expected_type=type_hints["cost_category"])
            check_type(argname="argument dimension", value=dimension, expected_type=type_hints["dimension"])
            check_type(argname="argument not_", value=not_, expected_type=type_hints["not_"])
            check_type(argname="argument or_", value=or_, expected_type=type_hints["or_"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if and_ is not None:
            self._values["and_"] = and_
        if cost_category is not None:
            self._values["cost_category"] = cost_category
        if dimension is not None:
            self._values["dimension"] = dimension
        if not_ is not None:
            self._values["not_"] = not_
        if or_ is not None:
            self._values["or_"] = or_
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def and_(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAwsCeTagsFilterAnd"]]]:
        '''and block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#and DataAwsCeTags#and}
        '''
        result = self._values.get("and_")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAwsCeTagsFilterAnd"]]], result)

    @builtins.property
    def cost_category(self) -> typing.Optional["DataAwsCeTagsFilterCostCategory"]:
        '''cost_category block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#cost_category DataAwsCeTags#cost_category}
        '''
        result = self._values.get("cost_category")
        return typing.cast(typing.Optional["DataAwsCeTagsFilterCostCategory"], result)

    @builtins.property
    def dimension(self) -> typing.Optional["DataAwsCeTagsFilterDimension"]:
        '''dimension block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#dimension DataAwsCeTags#dimension}
        '''
        result = self._values.get("dimension")
        return typing.cast(typing.Optional["DataAwsCeTagsFilterDimension"], result)

    @builtins.property
    def not_(self) -> typing.Optional["DataAwsCeTagsFilterNot"]:
        '''not block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#not DataAwsCeTags#not}
        '''
        result = self._values.get("not_")
        return typing.cast(typing.Optional["DataAwsCeTagsFilterNot"], result)

    @builtins.property
    def or_(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAwsCeTagsFilterOr"]]]:
        '''or block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#or DataAwsCeTags#or}
        '''
        result = self._values.get("or_")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAwsCeTagsFilterOr"]]], result)

    @builtins.property
    def tags(self) -> typing.Optional["DataAwsCeTagsFilterTags"]:
        '''tags block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#tags DataAwsCeTags#tags}
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional["DataAwsCeTagsFilterTags"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAwsCeTagsFilter(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.dataAwsCeTags.DataAwsCeTagsFilterAnd",
    jsii_struct_bases=[],
    name_mapping={
        "cost_category": "costCategory",
        "dimension": "dimension",
        "tags": "tags",
    },
)
class DataAwsCeTagsFilterAnd:
    def __init__(
        self,
        *,
        cost_category: typing.Optional[typing.Union["DataAwsCeTagsFilterAndCostCategory", typing.Dict[builtins.str, typing.Any]]] = None,
        dimension: typing.Optional[typing.Union["DataAwsCeTagsFilterAndDimension", typing.Dict[builtins.str, typing.Any]]] = None,
        tags: typing.Optional[typing.Union["DataAwsCeTagsFilterAndTags", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param cost_category: cost_category block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#cost_category DataAwsCeTags#cost_category}
        :param dimension: dimension block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#dimension DataAwsCeTags#dimension}
        :param tags: tags block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#tags DataAwsCeTags#tags}
        '''
        if isinstance(cost_category, dict):
            cost_category = DataAwsCeTagsFilterAndCostCategory(**cost_category)
        if isinstance(dimension, dict):
            dimension = DataAwsCeTagsFilterAndDimension(**dimension)
        if isinstance(tags, dict):
            tags = DataAwsCeTagsFilterAndTags(**tags)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9c249b5c212436c4e0f7b5ddf17eba497951d2dcb22a0caf3edd5deb2323a4c9)
            check_type(argname="argument cost_category", value=cost_category, expected_type=type_hints["cost_category"])
            check_type(argname="argument dimension", value=dimension, expected_type=type_hints["dimension"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if cost_category is not None:
            self._values["cost_category"] = cost_category
        if dimension is not None:
            self._values["dimension"] = dimension
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def cost_category(self) -> typing.Optional["DataAwsCeTagsFilterAndCostCategory"]:
        '''cost_category block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#cost_category DataAwsCeTags#cost_category}
        '''
        result = self._values.get("cost_category")
        return typing.cast(typing.Optional["DataAwsCeTagsFilterAndCostCategory"], result)

    @builtins.property
    def dimension(self) -> typing.Optional["DataAwsCeTagsFilterAndDimension"]:
        '''dimension block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#dimension DataAwsCeTags#dimension}
        '''
        result = self._values.get("dimension")
        return typing.cast(typing.Optional["DataAwsCeTagsFilterAndDimension"], result)

    @builtins.property
    def tags(self) -> typing.Optional["DataAwsCeTagsFilterAndTags"]:
        '''tags block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#tags DataAwsCeTags#tags}
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional["DataAwsCeTagsFilterAndTags"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAwsCeTagsFilterAnd(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.dataAwsCeTags.DataAwsCeTagsFilterAndCostCategory",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "match_options": "matchOptions", "values": "values"},
)
class DataAwsCeTagsFilterAndCostCategory:
    def __init__(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        match_options: typing.Optional[typing.Sequence[builtins.str]] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#key DataAwsCeTags#key}.
        :param match_options: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#match_options DataAwsCeTags#match_options}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#values DataAwsCeTags#values}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__776f81f61a9f40014900fc5b740754f6b19128ce270ae8740c5c077a4180b704)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument match_options", value=match_options, expected_type=type_hints["match_options"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if key is not None:
            self._values["key"] = key
        if match_options is not None:
            self._values["match_options"] = match_options
        if values is not None:
            self._values["values"] = values

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#key DataAwsCeTags#key}.'''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def match_options(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#match_options DataAwsCeTags#match_options}.'''
        result = self._values.get("match_options")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#values DataAwsCeTags#values}.'''
        result = self._values.get("values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAwsCeTagsFilterAndCostCategory(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAwsCeTagsFilterAndCostCategoryOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.dataAwsCeTags.DataAwsCeTagsFilterAndCostCategoryOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__954a47f0753aa83594b931dc9e8df948c125ceafcfa6ce674a1a1ad7e4f02fce)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetKey")
    def reset_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKey", []))

    @jsii.member(jsii_name="resetMatchOptions")
    def reset_match_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMatchOptions", []))

    @jsii.member(jsii_name="resetValues")
    def reset_values(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValues", []))

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="matchOptionsInput")
    def match_options_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "matchOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="valuesInput")
    def values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "valuesInput"))

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1c143b73a3326b9f9a7762058a07555281444a7eb8062c7ea5901b0cb32db5b3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="matchOptions")
    def match_options(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "matchOptions"))

    @match_options.setter
    def match_options(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f06798b59575b45077d61f17d9951b02389aa5d5b37dceef8b356299dde2c850)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "matchOptions", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9811010d8d00c2cbbd4be8d66e967747ee3cb246af9844b34fd36595e591d5e6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DataAwsCeTagsFilterAndCostCategory]:
        return typing.cast(typing.Optional[DataAwsCeTagsFilterAndCostCategory], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataAwsCeTagsFilterAndCostCategory],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__796a834fa4ea976b0d8572519a7825dbbc582c940f5adc08c5a85046ce6dda0b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.dataAwsCeTags.DataAwsCeTagsFilterAndDimension",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "match_options": "matchOptions", "values": "values"},
)
class DataAwsCeTagsFilterAndDimension:
    def __init__(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        match_options: typing.Optional[typing.Sequence[builtins.str]] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#key DataAwsCeTags#key}.
        :param match_options: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#match_options DataAwsCeTags#match_options}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#values DataAwsCeTags#values}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__715d352130c0cd8ffa4dec9c2533d4a3f5a1130747fadf00397dfa0d37d6b21f)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument match_options", value=match_options, expected_type=type_hints["match_options"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if key is not None:
            self._values["key"] = key
        if match_options is not None:
            self._values["match_options"] = match_options
        if values is not None:
            self._values["values"] = values

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#key DataAwsCeTags#key}.'''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def match_options(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#match_options DataAwsCeTags#match_options}.'''
        result = self._values.get("match_options")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#values DataAwsCeTags#values}.'''
        result = self._values.get("values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAwsCeTagsFilterAndDimension(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAwsCeTagsFilterAndDimensionOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.dataAwsCeTags.DataAwsCeTagsFilterAndDimensionOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7e0a58cad848a3c60398dd735600c9aca5ffc56a7ddcf83cf392849245eadc76)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetKey")
    def reset_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKey", []))

    @jsii.member(jsii_name="resetMatchOptions")
    def reset_match_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMatchOptions", []))

    @jsii.member(jsii_name="resetValues")
    def reset_values(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValues", []))

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="matchOptionsInput")
    def match_options_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "matchOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="valuesInput")
    def values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "valuesInput"))

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__77b7b699a6eb3e35f825e1a3ee1cdc11beeeefcc782568e15d15533226078be3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="matchOptions")
    def match_options(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "matchOptions"))

    @match_options.setter
    def match_options(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d7263944e188fbee2291ab86f13ac8eecd604bbb4d2df6f799dd3fcde9c792fb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "matchOptions", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__deefb1eadde8e6f6793214f5898edac1d069c347bb64055d5262de6d894bb77a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DataAwsCeTagsFilterAndDimension]:
        return typing.cast(typing.Optional[DataAwsCeTagsFilterAndDimension], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataAwsCeTagsFilterAndDimension],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6c771937e680b773ad29f04a410fa71be6dcc0206e554c41d01429c124dd585e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataAwsCeTagsFilterAndList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.dataAwsCeTags.DataAwsCeTagsFilterAndList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c024f2351aee74c8770a97812403856c0fba564a84117597ade304234e344f3a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "DataAwsCeTagsFilterAndOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__afaa98e3d8046b2f7c898143eb22cb6c122b020d05a41e37a350ca12e6fb9a32)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataAwsCeTagsFilterAndOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6f490cf09bb99ca9af2bc3755e422cb245b3ffdf1e7a5c6372e867062800bbaf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8bb9bf2990d3168d09a366bc4de5db400fb13369d7d95ceb96ee69b1e1ed72e5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6f4db1d24c69559363de4d314158115e20dea52199ff5593dee5723f6c966847)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAwsCeTagsFilterAnd]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAwsCeTagsFilterAnd]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAwsCeTagsFilterAnd]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e8dbfbceac194c36301d36fec2d0274846a3b6ec09ccc02197f57d01e05c3988)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataAwsCeTagsFilterAndOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.dataAwsCeTags.DataAwsCeTagsFilterAndOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0d6853821cab293b3aebda4b0376b2f7bf43bfe679c82f8d910c7286d9079abd)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putCostCategory")
    def put_cost_category(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        match_options: typing.Optional[typing.Sequence[builtins.str]] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#key DataAwsCeTags#key}.
        :param match_options: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#match_options DataAwsCeTags#match_options}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#values DataAwsCeTags#values}.
        '''
        value = DataAwsCeTagsFilterAndCostCategory(
            key=key, match_options=match_options, values=values
        )

        return typing.cast(None, jsii.invoke(self, "putCostCategory", [value]))

    @jsii.member(jsii_name="putDimension")
    def put_dimension(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        match_options: typing.Optional[typing.Sequence[builtins.str]] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#key DataAwsCeTags#key}.
        :param match_options: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#match_options DataAwsCeTags#match_options}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#values DataAwsCeTags#values}.
        '''
        value = DataAwsCeTagsFilterAndDimension(
            key=key, match_options=match_options, values=values
        )

        return typing.cast(None, jsii.invoke(self, "putDimension", [value]))

    @jsii.member(jsii_name="putTags")
    def put_tags(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        match_options: typing.Optional[typing.Sequence[builtins.str]] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#key DataAwsCeTags#key}.
        :param match_options: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#match_options DataAwsCeTags#match_options}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#values DataAwsCeTags#values}.
        '''
        value = DataAwsCeTagsFilterAndTags(
            key=key, match_options=match_options, values=values
        )

        return typing.cast(None, jsii.invoke(self, "putTags", [value]))

    @jsii.member(jsii_name="resetCostCategory")
    def reset_cost_category(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCostCategory", []))

    @jsii.member(jsii_name="resetDimension")
    def reset_dimension(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDimension", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @builtins.property
    @jsii.member(jsii_name="costCategory")
    def cost_category(self) -> DataAwsCeTagsFilterAndCostCategoryOutputReference:
        return typing.cast(DataAwsCeTagsFilterAndCostCategoryOutputReference, jsii.get(self, "costCategory"))

    @builtins.property
    @jsii.member(jsii_name="dimension")
    def dimension(self) -> DataAwsCeTagsFilterAndDimensionOutputReference:
        return typing.cast(DataAwsCeTagsFilterAndDimensionOutputReference, jsii.get(self, "dimension"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> "DataAwsCeTagsFilterAndTagsOutputReference":
        return typing.cast("DataAwsCeTagsFilterAndTagsOutputReference", jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="costCategoryInput")
    def cost_category_input(
        self,
    ) -> typing.Optional[DataAwsCeTagsFilterAndCostCategory]:
        return typing.cast(typing.Optional[DataAwsCeTagsFilterAndCostCategory], jsii.get(self, "costCategoryInput"))

    @builtins.property
    @jsii.member(jsii_name="dimensionInput")
    def dimension_input(self) -> typing.Optional[DataAwsCeTagsFilterAndDimension]:
        return typing.cast(typing.Optional[DataAwsCeTagsFilterAndDimension], jsii.get(self, "dimensionInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional["DataAwsCeTagsFilterAndTags"]:
        return typing.cast(typing.Optional["DataAwsCeTagsFilterAndTags"], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DataAwsCeTagsFilterAnd, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DataAwsCeTagsFilterAnd, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DataAwsCeTagsFilterAnd, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4f68bdf84b7a09235aadc11f56ae8042dc959045e9e1d461306dbbf814801f2b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.dataAwsCeTags.DataAwsCeTagsFilterAndTags",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "match_options": "matchOptions", "values": "values"},
)
class DataAwsCeTagsFilterAndTags:
    def __init__(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        match_options: typing.Optional[typing.Sequence[builtins.str]] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#key DataAwsCeTags#key}.
        :param match_options: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#match_options DataAwsCeTags#match_options}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#values DataAwsCeTags#values}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a55fe786c901d8efd1d4ae84a0f867d390689020a9bf3b0d1c859dd8a7a3998f)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument match_options", value=match_options, expected_type=type_hints["match_options"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if key is not None:
            self._values["key"] = key
        if match_options is not None:
            self._values["match_options"] = match_options
        if values is not None:
            self._values["values"] = values

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#key DataAwsCeTags#key}.'''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def match_options(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#match_options DataAwsCeTags#match_options}.'''
        result = self._values.get("match_options")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#values DataAwsCeTags#values}.'''
        result = self._values.get("values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAwsCeTagsFilterAndTags(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAwsCeTagsFilterAndTagsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.dataAwsCeTags.DataAwsCeTagsFilterAndTagsOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__23f8a32218b3d699323d5a63f8c3a2b38924e767e885ac99cafa55cb4de122f3)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetKey")
    def reset_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKey", []))

    @jsii.member(jsii_name="resetMatchOptions")
    def reset_match_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMatchOptions", []))

    @jsii.member(jsii_name="resetValues")
    def reset_values(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValues", []))

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="matchOptionsInput")
    def match_options_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "matchOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="valuesInput")
    def values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "valuesInput"))

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fde8615a4f38d743c24eb54434b57b89a7d1e3ae4c7db706f38e9706f192c756)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="matchOptions")
    def match_options(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "matchOptions"))

    @match_options.setter
    def match_options(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__27e074639d8b47fb1a2d6ad0bc6a539adde97d0805fcc43a980d9e5390a472e5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "matchOptions", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8874dd683b7c9683dd7f774ad652d09433d7cb63a3b8558ca0fb42daf8c0f455)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DataAwsCeTagsFilterAndTags]:
        return typing.cast(typing.Optional[DataAwsCeTagsFilterAndTags], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataAwsCeTagsFilterAndTags],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dd124fcf03bcbf19f064831ea2b76dbc80a38770e2e3e1991975fa3bc36f7c28)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.dataAwsCeTags.DataAwsCeTagsFilterCostCategory",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "match_options": "matchOptions", "values": "values"},
)
class DataAwsCeTagsFilterCostCategory:
    def __init__(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        match_options: typing.Optional[typing.Sequence[builtins.str]] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#key DataAwsCeTags#key}.
        :param match_options: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#match_options DataAwsCeTags#match_options}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#values DataAwsCeTags#values}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5bdce937e903123f3676b98d35e984765211ad37e01e9e0f2c2273a054ae756e)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument match_options", value=match_options, expected_type=type_hints["match_options"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if key is not None:
            self._values["key"] = key
        if match_options is not None:
            self._values["match_options"] = match_options
        if values is not None:
            self._values["values"] = values

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#key DataAwsCeTags#key}.'''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def match_options(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#match_options DataAwsCeTags#match_options}.'''
        result = self._values.get("match_options")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#values DataAwsCeTags#values}.'''
        result = self._values.get("values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAwsCeTagsFilterCostCategory(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAwsCeTagsFilterCostCategoryOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.dataAwsCeTags.DataAwsCeTagsFilterCostCategoryOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1f2dd646cf24472e7e8714de0aeea3663650ef8dfccf2e4b13990ebfe89b7094)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetKey")
    def reset_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKey", []))

    @jsii.member(jsii_name="resetMatchOptions")
    def reset_match_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMatchOptions", []))

    @jsii.member(jsii_name="resetValues")
    def reset_values(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValues", []))

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="matchOptionsInput")
    def match_options_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "matchOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="valuesInput")
    def values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "valuesInput"))

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bb7d22c9ee4318f06e051b8d1360828f3a20bb9edf914f659fc34f1bfc7725a9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="matchOptions")
    def match_options(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "matchOptions"))

    @match_options.setter
    def match_options(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0f970adabcce83501ae5d47d58e29d6395ff7e9d8aca4411ed2d0c7ac03642ac)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "matchOptions", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__407f927a57a93cb1d862e9122908c667c1d77fb4e936c5c12dd63fdfa95ee167)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DataAwsCeTagsFilterCostCategory]:
        return typing.cast(typing.Optional[DataAwsCeTagsFilterCostCategory], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataAwsCeTagsFilterCostCategory],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__09ed9778b32d0bcdac6bee10515b4cb96e2594dc54477dc8fa2a2a7ba39e6e10)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.dataAwsCeTags.DataAwsCeTagsFilterDimension",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "match_options": "matchOptions", "values": "values"},
)
class DataAwsCeTagsFilterDimension:
    def __init__(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        match_options: typing.Optional[typing.Sequence[builtins.str]] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#key DataAwsCeTags#key}.
        :param match_options: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#match_options DataAwsCeTags#match_options}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#values DataAwsCeTags#values}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__09ac5f3bf205a8d1187600ac7271094ba501bd725964011e518668506ac2bd40)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument match_options", value=match_options, expected_type=type_hints["match_options"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if key is not None:
            self._values["key"] = key
        if match_options is not None:
            self._values["match_options"] = match_options
        if values is not None:
            self._values["values"] = values

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#key DataAwsCeTags#key}.'''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def match_options(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#match_options DataAwsCeTags#match_options}.'''
        result = self._values.get("match_options")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#values DataAwsCeTags#values}.'''
        result = self._values.get("values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAwsCeTagsFilterDimension(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAwsCeTagsFilterDimensionOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.dataAwsCeTags.DataAwsCeTagsFilterDimensionOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c0ed891f755423fef9565757092530a16a9efc6128c922378a2947390848f3b6)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetKey")
    def reset_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKey", []))

    @jsii.member(jsii_name="resetMatchOptions")
    def reset_match_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMatchOptions", []))

    @jsii.member(jsii_name="resetValues")
    def reset_values(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValues", []))

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="matchOptionsInput")
    def match_options_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "matchOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="valuesInput")
    def values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "valuesInput"))

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5a52a5e50091a55d0e5cd20e410e4a9fb8a65e4f5f4cd2ea8cfe11a847167fe1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="matchOptions")
    def match_options(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "matchOptions"))

    @match_options.setter
    def match_options(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6dfa3c9d914fec0ea33d07ab62b50a62da6f5107ddd8e4185b7f50669bc1aa6a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "matchOptions", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c0eea3edd203ee1f00e349a11db2137ae0f05571390d029747889d88719dfbde)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DataAwsCeTagsFilterDimension]:
        return typing.cast(typing.Optional[DataAwsCeTagsFilterDimension], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataAwsCeTagsFilterDimension],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6115cda1bc62db1d5cdc6cfae6248210f3af2291c7bff5bc296c19ff22f7947f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.dataAwsCeTags.DataAwsCeTagsFilterNot",
    jsii_struct_bases=[],
    name_mapping={
        "cost_category": "costCategory",
        "dimension": "dimension",
        "tags": "tags",
    },
)
class DataAwsCeTagsFilterNot:
    def __init__(
        self,
        *,
        cost_category: typing.Optional[typing.Union["DataAwsCeTagsFilterNotCostCategory", typing.Dict[builtins.str, typing.Any]]] = None,
        dimension: typing.Optional[typing.Union["DataAwsCeTagsFilterNotDimension", typing.Dict[builtins.str, typing.Any]]] = None,
        tags: typing.Optional[typing.Union["DataAwsCeTagsFilterNotTags", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param cost_category: cost_category block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#cost_category DataAwsCeTags#cost_category}
        :param dimension: dimension block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#dimension DataAwsCeTags#dimension}
        :param tags: tags block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#tags DataAwsCeTags#tags}
        '''
        if isinstance(cost_category, dict):
            cost_category = DataAwsCeTagsFilterNotCostCategory(**cost_category)
        if isinstance(dimension, dict):
            dimension = DataAwsCeTagsFilterNotDimension(**dimension)
        if isinstance(tags, dict):
            tags = DataAwsCeTagsFilterNotTags(**tags)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a3854fe449096d200ab76ba47aa1e940d42537c412e2872187b7f1fd2f5aa210)
            check_type(argname="argument cost_category", value=cost_category, expected_type=type_hints["cost_category"])
            check_type(argname="argument dimension", value=dimension, expected_type=type_hints["dimension"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if cost_category is not None:
            self._values["cost_category"] = cost_category
        if dimension is not None:
            self._values["dimension"] = dimension
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def cost_category(self) -> typing.Optional["DataAwsCeTagsFilterNotCostCategory"]:
        '''cost_category block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#cost_category DataAwsCeTags#cost_category}
        '''
        result = self._values.get("cost_category")
        return typing.cast(typing.Optional["DataAwsCeTagsFilterNotCostCategory"], result)

    @builtins.property
    def dimension(self) -> typing.Optional["DataAwsCeTagsFilterNotDimension"]:
        '''dimension block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#dimension DataAwsCeTags#dimension}
        '''
        result = self._values.get("dimension")
        return typing.cast(typing.Optional["DataAwsCeTagsFilterNotDimension"], result)

    @builtins.property
    def tags(self) -> typing.Optional["DataAwsCeTagsFilterNotTags"]:
        '''tags block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#tags DataAwsCeTags#tags}
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional["DataAwsCeTagsFilterNotTags"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAwsCeTagsFilterNot(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.dataAwsCeTags.DataAwsCeTagsFilterNotCostCategory",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "match_options": "matchOptions", "values": "values"},
)
class DataAwsCeTagsFilterNotCostCategory:
    def __init__(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        match_options: typing.Optional[typing.Sequence[builtins.str]] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#key DataAwsCeTags#key}.
        :param match_options: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#match_options DataAwsCeTags#match_options}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#values DataAwsCeTags#values}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a6c54ffd43706056ca39b285917e4d1a59dd76fb00516dab3f82826326d48bb7)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument match_options", value=match_options, expected_type=type_hints["match_options"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if key is not None:
            self._values["key"] = key
        if match_options is not None:
            self._values["match_options"] = match_options
        if values is not None:
            self._values["values"] = values

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#key DataAwsCeTags#key}.'''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def match_options(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#match_options DataAwsCeTags#match_options}.'''
        result = self._values.get("match_options")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#values DataAwsCeTags#values}.'''
        result = self._values.get("values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAwsCeTagsFilterNotCostCategory(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAwsCeTagsFilterNotCostCategoryOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.dataAwsCeTags.DataAwsCeTagsFilterNotCostCategoryOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fe9f4a111017765d368bc6ca303c8f18125fb12bc920900c60e9d270588d6192)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetKey")
    def reset_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKey", []))

    @jsii.member(jsii_name="resetMatchOptions")
    def reset_match_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMatchOptions", []))

    @jsii.member(jsii_name="resetValues")
    def reset_values(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValues", []))

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="matchOptionsInput")
    def match_options_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "matchOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="valuesInput")
    def values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "valuesInput"))

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7dd949ea61cf85b13c7f5d237231d4e7bbefc982ccf745746f51f725940a9a50)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="matchOptions")
    def match_options(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "matchOptions"))

    @match_options.setter
    def match_options(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8acc2dc6a45fbc7077538f81f5b76e5291bc7a552fe2a2fd19508af6ab0f93ca)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "matchOptions", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__374b03371c9e16cd8fed0f61fe051b4f4d64c61d082e556decc6a45df1fe6613)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DataAwsCeTagsFilterNotCostCategory]:
        return typing.cast(typing.Optional[DataAwsCeTagsFilterNotCostCategory], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataAwsCeTagsFilterNotCostCategory],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__825a6188fca608814ec406fecd2754a0527614b4efbcc25cc65b7cab5669347c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.dataAwsCeTags.DataAwsCeTagsFilterNotDimension",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "match_options": "matchOptions", "values": "values"},
)
class DataAwsCeTagsFilterNotDimension:
    def __init__(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        match_options: typing.Optional[typing.Sequence[builtins.str]] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#key DataAwsCeTags#key}.
        :param match_options: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#match_options DataAwsCeTags#match_options}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#values DataAwsCeTags#values}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2609ce5ff59c39e6302eb8882aa3e1c48559b4a3acc2d8b6854fc00cc10aa34a)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument match_options", value=match_options, expected_type=type_hints["match_options"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if key is not None:
            self._values["key"] = key
        if match_options is not None:
            self._values["match_options"] = match_options
        if values is not None:
            self._values["values"] = values

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#key DataAwsCeTags#key}.'''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def match_options(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#match_options DataAwsCeTags#match_options}.'''
        result = self._values.get("match_options")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#values DataAwsCeTags#values}.'''
        result = self._values.get("values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAwsCeTagsFilterNotDimension(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAwsCeTagsFilterNotDimensionOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.dataAwsCeTags.DataAwsCeTagsFilterNotDimensionOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4fd601d9d6e5608829cd6b83f44cef3c10be280d65bbccbc0b083e7294050cfb)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetKey")
    def reset_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKey", []))

    @jsii.member(jsii_name="resetMatchOptions")
    def reset_match_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMatchOptions", []))

    @jsii.member(jsii_name="resetValues")
    def reset_values(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValues", []))

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="matchOptionsInput")
    def match_options_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "matchOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="valuesInput")
    def values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "valuesInput"))

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e5e36f8b0ab0f17b153360ca4a7eec73bf83dcf95034f642464a33e72b47d367)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="matchOptions")
    def match_options(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "matchOptions"))

    @match_options.setter
    def match_options(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__42e4ebccc6245a05045b64f59568d3eed7e4a2786cf58f32821cd39b75865651)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "matchOptions", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b8260bd87b637e665cc1e6addf152e7a5bc8bf6af8181d7cd71178a523e54408)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DataAwsCeTagsFilterNotDimension]:
        return typing.cast(typing.Optional[DataAwsCeTagsFilterNotDimension], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataAwsCeTagsFilterNotDimension],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__75f015dcfe90ca5e605f3a99fa68b426c0d7d8391672f9e03db1a619391180ef)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataAwsCeTagsFilterNotOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.dataAwsCeTags.DataAwsCeTagsFilterNotOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__552861e52930ccf110f7b39ac3e0640231885481e5c697efba85724a07419321)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putCostCategory")
    def put_cost_category(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        match_options: typing.Optional[typing.Sequence[builtins.str]] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#key DataAwsCeTags#key}.
        :param match_options: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#match_options DataAwsCeTags#match_options}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#values DataAwsCeTags#values}.
        '''
        value = DataAwsCeTagsFilterNotCostCategory(
            key=key, match_options=match_options, values=values
        )

        return typing.cast(None, jsii.invoke(self, "putCostCategory", [value]))

    @jsii.member(jsii_name="putDimension")
    def put_dimension(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        match_options: typing.Optional[typing.Sequence[builtins.str]] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#key DataAwsCeTags#key}.
        :param match_options: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#match_options DataAwsCeTags#match_options}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#values DataAwsCeTags#values}.
        '''
        value = DataAwsCeTagsFilterNotDimension(
            key=key, match_options=match_options, values=values
        )

        return typing.cast(None, jsii.invoke(self, "putDimension", [value]))

    @jsii.member(jsii_name="putTags")
    def put_tags(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        match_options: typing.Optional[typing.Sequence[builtins.str]] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#key DataAwsCeTags#key}.
        :param match_options: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#match_options DataAwsCeTags#match_options}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#values DataAwsCeTags#values}.
        '''
        value = DataAwsCeTagsFilterNotTags(
            key=key, match_options=match_options, values=values
        )

        return typing.cast(None, jsii.invoke(self, "putTags", [value]))

    @jsii.member(jsii_name="resetCostCategory")
    def reset_cost_category(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCostCategory", []))

    @jsii.member(jsii_name="resetDimension")
    def reset_dimension(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDimension", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @builtins.property
    @jsii.member(jsii_name="costCategory")
    def cost_category(self) -> DataAwsCeTagsFilterNotCostCategoryOutputReference:
        return typing.cast(DataAwsCeTagsFilterNotCostCategoryOutputReference, jsii.get(self, "costCategory"))

    @builtins.property
    @jsii.member(jsii_name="dimension")
    def dimension(self) -> DataAwsCeTagsFilterNotDimensionOutputReference:
        return typing.cast(DataAwsCeTagsFilterNotDimensionOutputReference, jsii.get(self, "dimension"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> "DataAwsCeTagsFilterNotTagsOutputReference":
        return typing.cast("DataAwsCeTagsFilterNotTagsOutputReference", jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="costCategoryInput")
    def cost_category_input(
        self,
    ) -> typing.Optional[DataAwsCeTagsFilterNotCostCategory]:
        return typing.cast(typing.Optional[DataAwsCeTagsFilterNotCostCategory], jsii.get(self, "costCategoryInput"))

    @builtins.property
    @jsii.member(jsii_name="dimensionInput")
    def dimension_input(self) -> typing.Optional[DataAwsCeTagsFilterNotDimension]:
        return typing.cast(typing.Optional[DataAwsCeTagsFilterNotDimension], jsii.get(self, "dimensionInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional["DataAwsCeTagsFilterNotTags"]:
        return typing.cast(typing.Optional["DataAwsCeTagsFilterNotTags"], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DataAwsCeTagsFilterNot]:
        return typing.cast(typing.Optional[DataAwsCeTagsFilterNot], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[DataAwsCeTagsFilterNot]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d750345dfbb70438e19e682dd21c8037f7631e22f02b2c459a4e6c5ec275d030)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.dataAwsCeTags.DataAwsCeTagsFilterNotTags",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "match_options": "matchOptions", "values": "values"},
)
class DataAwsCeTagsFilterNotTags:
    def __init__(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        match_options: typing.Optional[typing.Sequence[builtins.str]] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#key DataAwsCeTags#key}.
        :param match_options: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#match_options DataAwsCeTags#match_options}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#values DataAwsCeTags#values}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c99225f7114a5fead86920a140da0ffbfdf3c0a25e0ddfc0dc6f6818d0176b37)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument match_options", value=match_options, expected_type=type_hints["match_options"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if key is not None:
            self._values["key"] = key
        if match_options is not None:
            self._values["match_options"] = match_options
        if values is not None:
            self._values["values"] = values

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#key DataAwsCeTags#key}.'''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def match_options(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#match_options DataAwsCeTags#match_options}.'''
        result = self._values.get("match_options")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#values DataAwsCeTags#values}.'''
        result = self._values.get("values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAwsCeTagsFilterNotTags(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAwsCeTagsFilterNotTagsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.dataAwsCeTags.DataAwsCeTagsFilterNotTagsOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b951f3b8c7b0115992210e2e643c7e994c2e54d025849955cf211e81992e5136)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetKey")
    def reset_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKey", []))

    @jsii.member(jsii_name="resetMatchOptions")
    def reset_match_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMatchOptions", []))

    @jsii.member(jsii_name="resetValues")
    def reset_values(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValues", []))

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="matchOptionsInput")
    def match_options_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "matchOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="valuesInput")
    def values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "valuesInput"))

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5f98461df53731d4b9a9c6a2e12276697066f77acad2d1b5553598978d0abbac)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="matchOptions")
    def match_options(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "matchOptions"))

    @match_options.setter
    def match_options(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ae56bcf86af8011773686d87369fc6ac556c7039257114918e1400c1c9663487)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "matchOptions", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__900d89861b773a8f6abf6f76412e8dcbe93f978b8d5b4a89a03ac77607caee6a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DataAwsCeTagsFilterNotTags]:
        return typing.cast(typing.Optional[DataAwsCeTagsFilterNotTags], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataAwsCeTagsFilterNotTags],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c71d23634056c168cc30d2a0e66547e8234217de6686b35a02735e62b7124a7a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.dataAwsCeTags.DataAwsCeTagsFilterOr",
    jsii_struct_bases=[],
    name_mapping={
        "cost_category": "costCategory",
        "dimension": "dimension",
        "tags": "tags",
    },
)
class DataAwsCeTagsFilterOr:
    def __init__(
        self,
        *,
        cost_category: typing.Optional[typing.Union["DataAwsCeTagsFilterOrCostCategory", typing.Dict[builtins.str, typing.Any]]] = None,
        dimension: typing.Optional[typing.Union["DataAwsCeTagsFilterOrDimension", typing.Dict[builtins.str, typing.Any]]] = None,
        tags: typing.Optional[typing.Union["DataAwsCeTagsFilterOrTags", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param cost_category: cost_category block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#cost_category DataAwsCeTags#cost_category}
        :param dimension: dimension block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#dimension DataAwsCeTags#dimension}
        :param tags: tags block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#tags DataAwsCeTags#tags}
        '''
        if isinstance(cost_category, dict):
            cost_category = DataAwsCeTagsFilterOrCostCategory(**cost_category)
        if isinstance(dimension, dict):
            dimension = DataAwsCeTagsFilterOrDimension(**dimension)
        if isinstance(tags, dict):
            tags = DataAwsCeTagsFilterOrTags(**tags)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__27252865abef982091f8b7d4fc15a3a257d6a73549d9542411a6293214295074)
            check_type(argname="argument cost_category", value=cost_category, expected_type=type_hints["cost_category"])
            check_type(argname="argument dimension", value=dimension, expected_type=type_hints["dimension"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if cost_category is not None:
            self._values["cost_category"] = cost_category
        if dimension is not None:
            self._values["dimension"] = dimension
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def cost_category(self) -> typing.Optional["DataAwsCeTagsFilterOrCostCategory"]:
        '''cost_category block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#cost_category DataAwsCeTags#cost_category}
        '''
        result = self._values.get("cost_category")
        return typing.cast(typing.Optional["DataAwsCeTagsFilterOrCostCategory"], result)

    @builtins.property
    def dimension(self) -> typing.Optional["DataAwsCeTagsFilterOrDimension"]:
        '''dimension block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#dimension DataAwsCeTags#dimension}
        '''
        result = self._values.get("dimension")
        return typing.cast(typing.Optional["DataAwsCeTagsFilterOrDimension"], result)

    @builtins.property
    def tags(self) -> typing.Optional["DataAwsCeTagsFilterOrTags"]:
        '''tags block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#tags DataAwsCeTags#tags}
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional["DataAwsCeTagsFilterOrTags"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAwsCeTagsFilterOr(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.dataAwsCeTags.DataAwsCeTagsFilterOrCostCategory",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "match_options": "matchOptions", "values": "values"},
)
class DataAwsCeTagsFilterOrCostCategory:
    def __init__(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        match_options: typing.Optional[typing.Sequence[builtins.str]] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#key DataAwsCeTags#key}.
        :param match_options: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#match_options DataAwsCeTags#match_options}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#values DataAwsCeTags#values}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__12216440d97711004a1221cdce9f48f6f8e8d718688676125974c8967ae66369)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument match_options", value=match_options, expected_type=type_hints["match_options"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if key is not None:
            self._values["key"] = key
        if match_options is not None:
            self._values["match_options"] = match_options
        if values is not None:
            self._values["values"] = values

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#key DataAwsCeTags#key}.'''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def match_options(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#match_options DataAwsCeTags#match_options}.'''
        result = self._values.get("match_options")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#values DataAwsCeTags#values}.'''
        result = self._values.get("values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAwsCeTagsFilterOrCostCategory(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAwsCeTagsFilterOrCostCategoryOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.dataAwsCeTags.DataAwsCeTagsFilterOrCostCategoryOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c51a583e181ac243cea7fb1a263b9a3f5f2d0c1298e7bb89ac8a0dde5d78df62)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetKey")
    def reset_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKey", []))

    @jsii.member(jsii_name="resetMatchOptions")
    def reset_match_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMatchOptions", []))

    @jsii.member(jsii_name="resetValues")
    def reset_values(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValues", []))

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="matchOptionsInput")
    def match_options_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "matchOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="valuesInput")
    def values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "valuesInput"))

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__07535dbddd52354d4fb2333335d9318f92e412a0bc5e62480e7829684fa821eb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="matchOptions")
    def match_options(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "matchOptions"))

    @match_options.setter
    def match_options(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a6ff90a0671557b9d4e32468bd930f7d0b0faa44752e697fa2f7b11cc48d1b23)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "matchOptions", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__67bae31e4c9fad0c9ac7a101aa780e9e61afdd0dd99cbf9430658b5c0f2a76b4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DataAwsCeTagsFilterOrCostCategory]:
        return typing.cast(typing.Optional[DataAwsCeTagsFilterOrCostCategory], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataAwsCeTagsFilterOrCostCategory],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c24085d06711f980971d9c4e019c298474cfcf27f0de0c426a1962ece95df34d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.dataAwsCeTags.DataAwsCeTagsFilterOrDimension",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "match_options": "matchOptions", "values": "values"},
)
class DataAwsCeTagsFilterOrDimension:
    def __init__(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        match_options: typing.Optional[typing.Sequence[builtins.str]] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#key DataAwsCeTags#key}.
        :param match_options: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#match_options DataAwsCeTags#match_options}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#values DataAwsCeTags#values}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__92e37952e24f153dbec45b84c800177a5aa1757330fcece936e327d98ec8c59e)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument match_options", value=match_options, expected_type=type_hints["match_options"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if key is not None:
            self._values["key"] = key
        if match_options is not None:
            self._values["match_options"] = match_options
        if values is not None:
            self._values["values"] = values

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#key DataAwsCeTags#key}.'''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def match_options(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#match_options DataAwsCeTags#match_options}.'''
        result = self._values.get("match_options")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#values DataAwsCeTags#values}.'''
        result = self._values.get("values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAwsCeTagsFilterOrDimension(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAwsCeTagsFilterOrDimensionOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.dataAwsCeTags.DataAwsCeTagsFilterOrDimensionOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__45c076b8986c3ff47e02a1dd714c04bc5ff19f1cfae5c58984d4eab8f5ec5593)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetKey")
    def reset_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKey", []))

    @jsii.member(jsii_name="resetMatchOptions")
    def reset_match_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMatchOptions", []))

    @jsii.member(jsii_name="resetValues")
    def reset_values(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValues", []))

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="matchOptionsInput")
    def match_options_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "matchOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="valuesInput")
    def values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "valuesInput"))

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__910c7f9cb815a8b1bf62e3e547a9f71852813842397e0d587c7be837641334e4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="matchOptions")
    def match_options(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "matchOptions"))

    @match_options.setter
    def match_options(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d64a573cedad135f78bd350fac9b4535f2435256096db50f23017875e26b4b7c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "matchOptions", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__74862576fbd0471e085e84e321ccb6b71136f6f30dac90936bf638180f70507e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DataAwsCeTagsFilterOrDimension]:
        return typing.cast(typing.Optional[DataAwsCeTagsFilterOrDimension], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataAwsCeTagsFilterOrDimension],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ca885e8a88c9c984863512eed341f6c8583740d87146633974f6eea3eaa5367e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataAwsCeTagsFilterOrList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.dataAwsCeTags.DataAwsCeTagsFilterOrList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__04abb6c36b096675d445df43c1ac58cff5e6b6a81039ec8c36dd2022a1e3d481)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "DataAwsCeTagsFilterOrOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5551997114c8ff12803daf63f56ca3dd5652ebb91953e466323aeb1408c2213c)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataAwsCeTagsFilterOrOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__837e3c7becd0179020d65ee3d1177665c8b05e005778fa78b7d83bff71cc0457)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__789e0d6a2b27e14f91cd417aafbbf42fb49593cdcb2ec8dae39473c6891caf28)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b8945663877ce56f506b324eed538f133b1d88b1fc2c9ce9edbc3fb9a4d097fc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAwsCeTagsFilterOr]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAwsCeTagsFilterOr]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAwsCeTagsFilterOr]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__36a0ab99707d7f22f0b15c67cc927dab26f7de2d12f49b0ff0a97b3e51244af0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataAwsCeTagsFilterOrOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.dataAwsCeTags.DataAwsCeTagsFilterOrOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dddaa11b8804c6ff6803fb4a421ad311455e955ab68024786f084e9d3c44465b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putCostCategory")
    def put_cost_category(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        match_options: typing.Optional[typing.Sequence[builtins.str]] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#key DataAwsCeTags#key}.
        :param match_options: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#match_options DataAwsCeTags#match_options}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#values DataAwsCeTags#values}.
        '''
        value = DataAwsCeTagsFilterOrCostCategory(
            key=key, match_options=match_options, values=values
        )

        return typing.cast(None, jsii.invoke(self, "putCostCategory", [value]))

    @jsii.member(jsii_name="putDimension")
    def put_dimension(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        match_options: typing.Optional[typing.Sequence[builtins.str]] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#key DataAwsCeTags#key}.
        :param match_options: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#match_options DataAwsCeTags#match_options}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#values DataAwsCeTags#values}.
        '''
        value = DataAwsCeTagsFilterOrDimension(
            key=key, match_options=match_options, values=values
        )

        return typing.cast(None, jsii.invoke(self, "putDimension", [value]))

    @jsii.member(jsii_name="putTags")
    def put_tags(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        match_options: typing.Optional[typing.Sequence[builtins.str]] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#key DataAwsCeTags#key}.
        :param match_options: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#match_options DataAwsCeTags#match_options}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#values DataAwsCeTags#values}.
        '''
        value = DataAwsCeTagsFilterOrTags(
            key=key, match_options=match_options, values=values
        )

        return typing.cast(None, jsii.invoke(self, "putTags", [value]))

    @jsii.member(jsii_name="resetCostCategory")
    def reset_cost_category(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCostCategory", []))

    @jsii.member(jsii_name="resetDimension")
    def reset_dimension(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDimension", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @builtins.property
    @jsii.member(jsii_name="costCategory")
    def cost_category(self) -> DataAwsCeTagsFilterOrCostCategoryOutputReference:
        return typing.cast(DataAwsCeTagsFilterOrCostCategoryOutputReference, jsii.get(self, "costCategory"))

    @builtins.property
    @jsii.member(jsii_name="dimension")
    def dimension(self) -> DataAwsCeTagsFilterOrDimensionOutputReference:
        return typing.cast(DataAwsCeTagsFilterOrDimensionOutputReference, jsii.get(self, "dimension"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> "DataAwsCeTagsFilterOrTagsOutputReference":
        return typing.cast("DataAwsCeTagsFilterOrTagsOutputReference", jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="costCategoryInput")
    def cost_category_input(self) -> typing.Optional[DataAwsCeTagsFilterOrCostCategory]:
        return typing.cast(typing.Optional[DataAwsCeTagsFilterOrCostCategory], jsii.get(self, "costCategoryInput"))

    @builtins.property
    @jsii.member(jsii_name="dimensionInput")
    def dimension_input(self) -> typing.Optional[DataAwsCeTagsFilterOrDimension]:
        return typing.cast(typing.Optional[DataAwsCeTagsFilterOrDimension], jsii.get(self, "dimensionInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional["DataAwsCeTagsFilterOrTags"]:
        return typing.cast(typing.Optional["DataAwsCeTagsFilterOrTags"], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DataAwsCeTagsFilterOr, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DataAwsCeTagsFilterOr, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DataAwsCeTagsFilterOr, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dbcd46614d8c3bfcbcc93210ce0b7e3c0e743181266e4872ac6d8344616343d5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.dataAwsCeTags.DataAwsCeTagsFilterOrTags",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "match_options": "matchOptions", "values": "values"},
)
class DataAwsCeTagsFilterOrTags:
    def __init__(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        match_options: typing.Optional[typing.Sequence[builtins.str]] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#key DataAwsCeTags#key}.
        :param match_options: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#match_options DataAwsCeTags#match_options}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#values DataAwsCeTags#values}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7c294b64f83dfa356caed3a9bfd84aa5d69c315ebca158449f21459412ccd7f7)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument match_options", value=match_options, expected_type=type_hints["match_options"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if key is not None:
            self._values["key"] = key
        if match_options is not None:
            self._values["match_options"] = match_options
        if values is not None:
            self._values["values"] = values

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#key DataAwsCeTags#key}.'''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def match_options(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#match_options DataAwsCeTags#match_options}.'''
        result = self._values.get("match_options")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#values DataAwsCeTags#values}.'''
        result = self._values.get("values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAwsCeTagsFilterOrTags(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAwsCeTagsFilterOrTagsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.dataAwsCeTags.DataAwsCeTagsFilterOrTagsOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2110a0264b444f4e8c0acf256dbdb168418071dae219b6bdef63d514f431a432)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetKey")
    def reset_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKey", []))

    @jsii.member(jsii_name="resetMatchOptions")
    def reset_match_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMatchOptions", []))

    @jsii.member(jsii_name="resetValues")
    def reset_values(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValues", []))

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="matchOptionsInput")
    def match_options_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "matchOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="valuesInput")
    def values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "valuesInput"))

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7ecff8fff001c6957edeb227116b80db953e65c1111bddbc5e539feb5f79884d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="matchOptions")
    def match_options(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "matchOptions"))

    @match_options.setter
    def match_options(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e7cfef665e1cdd67781c5441e4c716e2f3efdbb22e1ba1fbbd39f41815ebb5f8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "matchOptions", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__220ac06b8b5bebf8890dfae308b18848003fb38a2585b75886b6cb570037b8f1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DataAwsCeTagsFilterOrTags]:
        return typing.cast(typing.Optional[DataAwsCeTagsFilterOrTags], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[DataAwsCeTagsFilterOrTags]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__974251e0ce76d3d24ee205211fb1ef559af3f787c1a37f0ccdc40b5fb69ba4ca)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataAwsCeTagsFilterOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.dataAwsCeTags.DataAwsCeTagsFilterOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6d1c7648d5383eb93a557f420fdc9528c6e342f028f2d4dd2d485c7b2752d84d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAnd")
    def put_and(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAwsCeTagsFilterAnd, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3060121ba8c3ffc8fe9501119d254e3d96833ffece02820c49db0662819c5448)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAnd", [value]))

    @jsii.member(jsii_name="putCostCategory")
    def put_cost_category(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        match_options: typing.Optional[typing.Sequence[builtins.str]] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#key DataAwsCeTags#key}.
        :param match_options: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#match_options DataAwsCeTags#match_options}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#values DataAwsCeTags#values}.
        '''
        value = DataAwsCeTagsFilterCostCategory(
            key=key, match_options=match_options, values=values
        )

        return typing.cast(None, jsii.invoke(self, "putCostCategory", [value]))

    @jsii.member(jsii_name="putDimension")
    def put_dimension(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        match_options: typing.Optional[typing.Sequence[builtins.str]] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#key DataAwsCeTags#key}.
        :param match_options: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#match_options DataAwsCeTags#match_options}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#values DataAwsCeTags#values}.
        '''
        value = DataAwsCeTagsFilterDimension(
            key=key, match_options=match_options, values=values
        )

        return typing.cast(None, jsii.invoke(self, "putDimension", [value]))

    @jsii.member(jsii_name="putNot")
    def put_not(
        self,
        *,
        cost_category: typing.Optional[typing.Union[DataAwsCeTagsFilterNotCostCategory, typing.Dict[builtins.str, typing.Any]]] = None,
        dimension: typing.Optional[typing.Union[DataAwsCeTagsFilterNotDimension, typing.Dict[builtins.str, typing.Any]]] = None,
        tags: typing.Optional[typing.Union[DataAwsCeTagsFilterNotTags, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param cost_category: cost_category block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#cost_category DataAwsCeTags#cost_category}
        :param dimension: dimension block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#dimension DataAwsCeTags#dimension}
        :param tags: tags block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#tags DataAwsCeTags#tags}
        '''
        value = DataAwsCeTagsFilterNot(
            cost_category=cost_category, dimension=dimension, tags=tags
        )

        return typing.cast(None, jsii.invoke(self, "putNot", [value]))

    @jsii.member(jsii_name="putOr")
    def put_or(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAwsCeTagsFilterOr, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3f06c94420f8fd43649f05b119f3913d11235527d7a6687a5b5c44e8bf8801d2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putOr", [value]))

    @jsii.member(jsii_name="putTags")
    def put_tags(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        match_options: typing.Optional[typing.Sequence[builtins.str]] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#key DataAwsCeTags#key}.
        :param match_options: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#match_options DataAwsCeTags#match_options}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#values DataAwsCeTags#values}.
        '''
        value = DataAwsCeTagsFilterTags(
            key=key, match_options=match_options, values=values
        )

        return typing.cast(None, jsii.invoke(self, "putTags", [value]))

    @jsii.member(jsii_name="resetAnd")
    def reset_and(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAnd", []))

    @jsii.member(jsii_name="resetCostCategory")
    def reset_cost_category(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCostCategory", []))

    @jsii.member(jsii_name="resetDimension")
    def reset_dimension(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDimension", []))

    @jsii.member(jsii_name="resetNot")
    def reset_not(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNot", []))

    @jsii.member(jsii_name="resetOr")
    def reset_or(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOr", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @builtins.property
    @jsii.member(jsii_name="and")
    def and_(self) -> DataAwsCeTagsFilterAndList:
        return typing.cast(DataAwsCeTagsFilterAndList, jsii.get(self, "and"))

    @builtins.property
    @jsii.member(jsii_name="costCategory")
    def cost_category(self) -> DataAwsCeTagsFilterCostCategoryOutputReference:
        return typing.cast(DataAwsCeTagsFilterCostCategoryOutputReference, jsii.get(self, "costCategory"))

    @builtins.property
    @jsii.member(jsii_name="dimension")
    def dimension(self) -> DataAwsCeTagsFilterDimensionOutputReference:
        return typing.cast(DataAwsCeTagsFilterDimensionOutputReference, jsii.get(self, "dimension"))

    @builtins.property
    @jsii.member(jsii_name="not")
    def not_(self) -> DataAwsCeTagsFilterNotOutputReference:
        return typing.cast(DataAwsCeTagsFilterNotOutputReference, jsii.get(self, "not"))

    @builtins.property
    @jsii.member(jsii_name="or")
    def or_(self) -> DataAwsCeTagsFilterOrList:
        return typing.cast(DataAwsCeTagsFilterOrList, jsii.get(self, "or"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> "DataAwsCeTagsFilterTagsOutputReference":
        return typing.cast("DataAwsCeTagsFilterTagsOutputReference", jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="andInput")
    def and_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAwsCeTagsFilterAnd]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAwsCeTagsFilterAnd]]], jsii.get(self, "andInput"))

    @builtins.property
    @jsii.member(jsii_name="costCategoryInput")
    def cost_category_input(self) -> typing.Optional[DataAwsCeTagsFilterCostCategory]:
        return typing.cast(typing.Optional[DataAwsCeTagsFilterCostCategory], jsii.get(self, "costCategoryInput"))

    @builtins.property
    @jsii.member(jsii_name="dimensionInput")
    def dimension_input(self) -> typing.Optional[DataAwsCeTagsFilterDimension]:
        return typing.cast(typing.Optional[DataAwsCeTagsFilterDimension], jsii.get(self, "dimensionInput"))

    @builtins.property
    @jsii.member(jsii_name="notInput")
    def not_input(self) -> typing.Optional[DataAwsCeTagsFilterNot]:
        return typing.cast(typing.Optional[DataAwsCeTagsFilterNot], jsii.get(self, "notInput"))

    @builtins.property
    @jsii.member(jsii_name="orInput")
    def or_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAwsCeTagsFilterOr]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAwsCeTagsFilterOr]]], jsii.get(self, "orInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional["DataAwsCeTagsFilterTags"]:
        return typing.cast(typing.Optional["DataAwsCeTagsFilterTags"], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DataAwsCeTagsFilter]:
        return typing.cast(typing.Optional[DataAwsCeTagsFilter], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[DataAwsCeTagsFilter]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__128e349319d22f10cbb1c89eba80f01266dc6e5fba8984bc93eb0792146d05ee)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.dataAwsCeTags.DataAwsCeTagsFilterTags",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "match_options": "matchOptions", "values": "values"},
)
class DataAwsCeTagsFilterTags:
    def __init__(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        match_options: typing.Optional[typing.Sequence[builtins.str]] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#key DataAwsCeTags#key}.
        :param match_options: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#match_options DataAwsCeTags#match_options}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#values DataAwsCeTags#values}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1b2f496a1887d944a84bcf4a6ce5681421a7cb036687e766579c9b7ecf2abc15)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument match_options", value=match_options, expected_type=type_hints["match_options"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if key is not None:
            self._values["key"] = key
        if match_options is not None:
            self._values["match_options"] = match_options
        if values is not None:
            self._values["values"] = values

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#key DataAwsCeTags#key}.'''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def match_options(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#match_options DataAwsCeTags#match_options}.'''
        result = self._values.get("match_options")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#values DataAwsCeTags#values}.'''
        result = self._values.get("values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAwsCeTagsFilterTags(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAwsCeTagsFilterTagsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.dataAwsCeTags.DataAwsCeTagsFilterTagsOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__545b000e3ab88733ac6cf2bbf49c67afa5e322b776f8d4229eb5d002e679e633)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetKey")
    def reset_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKey", []))

    @jsii.member(jsii_name="resetMatchOptions")
    def reset_match_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMatchOptions", []))

    @jsii.member(jsii_name="resetValues")
    def reset_values(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValues", []))

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="matchOptionsInput")
    def match_options_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "matchOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="valuesInput")
    def values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "valuesInput"))

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f49bcb12c642e3d71166a124e36f9fa70a3d977dc8d1cbeb13be036f801ed840)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="matchOptions")
    def match_options(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "matchOptions"))

    @match_options.setter
    def match_options(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dc2efbff5d8de9b853153a78e4f9c38a9d0ce6c0b7c556499e7591c34c90dc33)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "matchOptions", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0357c65985f90fee9805318977664797228bd8f02eb77cb3186df1c1942fc27c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DataAwsCeTagsFilterTags]:
        return typing.cast(typing.Optional[DataAwsCeTagsFilterTags], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[DataAwsCeTagsFilterTags]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5b731ae38bfde0db9842c3393cdd9de680a8f7c74a431e0273db6b74e9550b11)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.dataAwsCeTags.DataAwsCeTagsSortBy",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "sort_order": "sortOrder"},
)
class DataAwsCeTagsSortBy:
    def __init__(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        sort_order: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#key DataAwsCeTags#key}.
        :param sort_order: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#sort_order DataAwsCeTags#sort_order}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b8838cad26be5f6fa548b3944779c03f40b6ee18fa475ffe832d7328e52e6a1d)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument sort_order", value=sort_order, expected_type=type_hints["sort_order"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if key is not None:
            self._values["key"] = key
        if sort_order is not None:
            self._values["sort_order"] = sort_order

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#key DataAwsCeTags#key}.'''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sort_order(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#sort_order DataAwsCeTags#sort_order}.'''
        result = self._values.get("sort_order")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAwsCeTagsSortBy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAwsCeTagsSortByList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.dataAwsCeTags.DataAwsCeTagsSortByList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__005cedf17f793a9d3a4378eb67709255f35fec44cf70555867a92f7c6d8100b7)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "DataAwsCeTagsSortByOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__42f2728b1db7f055cae0976a213f34f3e32c152b49f6a568fbaf6b798f0a2a01)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataAwsCeTagsSortByOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__abc35fa9db450bf53af55a56d60315b0929e423c8b1f64e3ef4393f6c0f0bb81)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a681fb260dcf67a1a39559cecca628b6845edfa0f5d18b6e9ca27d974bd7dec3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c4efb7625b0136daf6c07bc153c36d414557cd55355a39157a5fb45de00b7323)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAwsCeTagsSortBy]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAwsCeTagsSortBy]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAwsCeTagsSortBy]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f562cf51f28137c28c229673674cd4e6b1df17f3a6773f9155d071edd20c43db)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataAwsCeTagsSortByOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.dataAwsCeTags.DataAwsCeTagsSortByOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a4c6a48e2b3d4367bbd11035490942ceab1d4ce358efb46f686774d88027325f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetKey")
    def reset_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKey", []))

    @jsii.member(jsii_name="resetSortOrder")
    def reset_sort_order(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSortOrder", []))

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="sortOrderInput")
    def sort_order_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sortOrderInput"))

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a42b040ba0ffb6298324b8ba9c5c42e178a1650967edd9a5e7d59d4e5607168a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="sortOrder")
    def sort_order(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sortOrder"))

    @sort_order.setter
    def sort_order(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__11270a2a74e001c64c9a1617528d9b60319a1906a0210dd052b71358b7601aa3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sortOrder", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DataAwsCeTagsSortBy, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DataAwsCeTagsSortBy, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DataAwsCeTagsSortBy, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9ecf585a63b7d3d44b22c2b859db4196a6f16482bcaf00fe16fc5c5936848f4b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.dataAwsCeTags.DataAwsCeTagsTimePeriod",
    jsii_struct_bases=[],
    name_mapping={"end": "end", "start": "start"},
)
class DataAwsCeTagsTimePeriod:
    def __init__(self, *, end: builtins.str, start: builtins.str) -> None:
        '''
        :param end: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#end DataAwsCeTags#end}.
        :param start: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#start DataAwsCeTags#start}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f74b314690e24282b2b25a8a0893cc196570e383bf04ab46fe33e99f64dde31e)
            check_type(argname="argument end", value=end, expected_type=type_hints["end"])
            check_type(argname="argument start", value=start, expected_type=type_hints["start"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "end": end,
            "start": start,
        }

    @builtins.property
    def end(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#end DataAwsCeTags#end}.'''
        result = self._values.get("end")
        assert result is not None, "Required property 'end' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def start(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#start DataAwsCeTags#start}.'''
        result = self._values.get("start")
        assert result is not None, "Required property 'start' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAwsCeTagsTimePeriod(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAwsCeTagsTimePeriodOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.dataAwsCeTags.DataAwsCeTagsTimePeriodOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__915cf174913eb9adf2f09ef60651ea441efb42a42f2dc059e2fbe03b714fdd23)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="endInput")
    def end_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "endInput"))

    @builtins.property
    @jsii.member(jsii_name="startInput")
    def start_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "startInput"))

    @builtins.property
    @jsii.member(jsii_name="end")
    def end(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "end"))

    @end.setter
    def end(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__705c33fb0a1f05c9715595643aac5ea518178ac5d696ad2917a471d832431379)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "end", value)

    @builtins.property
    @jsii.member(jsii_name="start")
    def start(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "start"))

    @start.setter
    def start(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ff069614b257386a6be9413cca9ab574a4317573a155434e40a7b84684314c66)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "start", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DataAwsCeTagsTimePeriod]:
        return typing.cast(typing.Optional[DataAwsCeTagsTimePeriod], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[DataAwsCeTagsTimePeriod]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c217d373607c3f5defdcaa5a3238ae8096d44de5a1a89dfc72b58844d1ee137c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "DataAwsCeTags",
    "DataAwsCeTagsConfig",
    "DataAwsCeTagsFilter",
    "DataAwsCeTagsFilterAnd",
    "DataAwsCeTagsFilterAndCostCategory",
    "DataAwsCeTagsFilterAndCostCategoryOutputReference",
    "DataAwsCeTagsFilterAndDimension",
    "DataAwsCeTagsFilterAndDimensionOutputReference",
    "DataAwsCeTagsFilterAndList",
    "DataAwsCeTagsFilterAndOutputReference",
    "DataAwsCeTagsFilterAndTags",
    "DataAwsCeTagsFilterAndTagsOutputReference",
    "DataAwsCeTagsFilterCostCategory",
    "DataAwsCeTagsFilterCostCategoryOutputReference",
    "DataAwsCeTagsFilterDimension",
    "DataAwsCeTagsFilterDimensionOutputReference",
    "DataAwsCeTagsFilterNot",
    "DataAwsCeTagsFilterNotCostCategory",
    "DataAwsCeTagsFilterNotCostCategoryOutputReference",
    "DataAwsCeTagsFilterNotDimension",
    "DataAwsCeTagsFilterNotDimensionOutputReference",
    "DataAwsCeTagsFilterNotOutputReference",
    "DataAwsCeTagsFilterNotTags",
    "DataAwsCeTagsFilterNotTagsOutputReference",
    "DataAwsCeTagsFilterOr",
    "DataAwsCeTagsFilterOrCostCategory",
    "DataAwsCeTagsFilterOrCostCategoryOutputReference",
    "DataAwsCeTagsFilterOrDimension",
    "DataAwsCeTagsFilterOrDimensionOutputReference",
    "DataAwsCeTagsFilterOrList",
    "DataAwsCeTagsFilterOrOutputReference",
    "DataAwsCeTagsFilterOrTags",
    "DataAwsCeTagsFilterOrTagsOutputReference",
    "DataAwsCeTagsFilterOutputReference",
    "DataAwsCeTagsFilterTags",
    "DataAwsCeTagsFilterTagsOutputReference",
    "DataAwsCeTagsSortBy",
    "DataAwsCeTagsSortByList",
    "DataAwsCeTagsSortByOutputReference",
    "DataAwsCeTagsTimePeriod",
    "DataAwsCeTagsTimePeriodOutputReference",
]

publication.publish()

def _typecheckingstub__667a4290670c8642e77287d6f96f41ff5782a1fcc3790536d05070713877dcad(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    time_period: typing.Union[DataAwsCeTagsTimePeriod, typing.Dict[builtins.str, typing.Any]],
    filter: typing.Optional[typing.Union[DataAwsCeTagsFilter, typing.Dict[builtins.str, typing.Any]]] = None,
    id: typing.Optional[builtins.str] = None,
    search_string: typing.Optional[builtins.str] = None,
    sort_by: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAwsCeTagsSortBy, typing.Dict[builtins.str, typing.Any]]]]] = None,
    tag_key: typing.Optional[builtins.str] = None,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__47fc611d46d4baa1fcab8358f9444bbe04ca61efc2e7e09fa0b41b929301f809(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAwsCeTagsSortBy, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__021a152aa25ff3db1bc9655df6bf81b235d0fe675e2ff4fa65805c5bc8f6daea(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__044656f1cee5cbdbcb3cbd49c8a917b9feb84a776ff81dfb554c95bbeb184440(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d2a655c3fa75a1984ff8549b1f677016cf3e554f5eb5894835c184e8eb31f44(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e5bd96f2a3880010cc9f0d34c2fe1c2375a3b7c96a10ca408423c9e990d01c44(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    time_period: typing.Union[DataAwsCeTagsTimePeriod, typing.Dict[builtins.str, typing.Any]],
    filter: typing.Optional[typing.Union[DataAwsCeTagsFilter, typing.Dict[builtins.str, typing.Any]]] = None,
    id: typing.Optional[builtins.str] = None,
    search_string: typing.Optional[builtins.str] = None,
    sort_by: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAwsCeTagsSortBy, typing.Dict[builtins.str, typing.Any]]]]] = None,
    tag_key: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c166be0dbd327fcbc6f1bd0288e92351a4a7e955fd05982f2a40880d4d758a2(
    *,
    and_: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAwsCeTagsFilterAnd, typing.Dict[builtins.str, typing.Any]]]]] = None,
    cost_category: typing.Optional[typing.Union[DataAwsCeTagsFilterCostCategory, typing.Dict[builtins.str, typing.Any]]] = None,
    dimension: typing.Optional[typing.Union[DataAwsCeTagsFilterDimension, typing.Dict[builtins.str, typing.Any]]] = None,
    not_: typing.Optional[typing.Union[DataAwsCeTagsFilterNot, typing.Dict[builtins.str, typing.Any]]] = None,
    or_: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAwsCeTagsFilterOr, typing.Dict[builtins.str, typing.Any]]]]] = None,
    tags: typing.Optional[typing.Union[DataAwsCeTagsFilterTags, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c249b5c212436c4e0f7b5ddf17eba497951d2dcb22a0caf3edd5deb2323a4c9(
    *,
    cost_category: typing.Optional[typing.Union[DataAwsCeTagsFilterAndCostCategory, typing.Dict[builtins.str, typing.Any]]] = None,
    dimension: typing.Optional[typing.Union[DataAwsCeTagsFilterAndDimension, typing.Dict[builtins.str, typing.Any]]] = None,
    tags: typing.Optional[typing.Union[DataAwsCeTagsFilterAndTags, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__776f81f61a9f40014900fc5b740754f6b19128ce270ae8740c5c077a4180b704(
    *,
    key: typing.Optional[builtins.str] = None,
    match_options: typing.Optional[typing.Sequence[builtins.str]] = None,
    values: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__954a47f0753aa83594b931dc9e8df948c125ceafcfa6ce674a1a1ad7e4f02fce(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1c143b73a3326b9f9a7762058a07555281444a7eb8062c7ea5901b0cb32db5b3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f06798b59575b45077d61f17d9951b02389aa5d5b37dceef8b356299dde2c850(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9811010d8d00c2cbbd4be8d66e967747ee3cb246af9844b34fd36595e591d5e6(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__796a834fa4ea976b0d8572519a7825dbbc582c940f5adc08c5a85046ce6dda0b(
    value: typing.Optional[DataAwsCeTagsFilterAndCostCategory],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__715d352130c0cd8ffa4dec9c2533d4a3f5a1130747fadf00397dfa0d37d6b21f(
    *,
    key: typing.Optional[builtins.str] = None,
    match_options: typing.Optional[typing.Sequence[builtins.str]] = None,
    values: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7e0a58cad848a3c60398dd735600c9aca5ffc56a7ddcf83cf392849245eadc76(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__77b7b699a6eb3e35f825e1a3ee1cdc11beeeefcc782568e15d15533226078be3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d7263944e188fbee2291ab86f13ac8eecd604bbb4d2df6f799dd3fcde9c792fb(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__deefb1eadde8e6f6793214f5898edac1d069c347bb64055d5262de6d894bb77a(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6c771937e680b773ad29f04a410fa71be6dcc0206e554c41d01429c124dd585e(
    value: typing.Optional[DataAwsCeTagsFilterAndDimension],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c024f2351aee74c8770a97812403856c0fba564a84117597ade304234e344f3a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__afaa98e3d8046b2f7c898143eb22cb6c122b020d05a41e37a350ca12e6fb9a32(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f490cf09bb99ca9af2bc3755e422cb245b3ffdf1e7a5c6372e867062800bbaf(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8bb9bf2990d3168d09a366bc4de5db400fb13369d7d95ceb96ee69b1e1ed72e5(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f4db1d24c69559363de4d314158115e20dea52199ff5593dee5723f6c966847(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e8dbfbceac194c36301d36fec2d0274846a3b6ec09ccc02197f57d01e05c3988(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAwsCeTagsFilterAnd]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d6853821cab293b3aebda4b0376b2f7bf43bfe679c82f8d910c7286d9079abd(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f68bdf84b7a09235aadc11f56ae8042dc959045e9e1d461306dbbf814801f2b(
    value: typing.Optional[typing.Union[DataAwsCeTagsFilterAnd, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a55fe786c901d8efd1d4ae84a0f867d390689020a9bf3b0d1c859dd8a7a3998f(
    *,
    key: typing.Optional[builtins.str] = None,
    match_options: typing.Optional[typing.Sequence[builtins.str]] = None,
    values: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__23f8a32218b3d699323d5a63f8c3a2b38924e767e885ac99cafa55cb4de122f3(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fde8615a4f38d743c24eb54434b57b89a7d1e3ae4c7db706f38e9706f192c756(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__27e074639d8b47fb1a2d6ad0bc6a539adde97d0805fcc43a980d9e5390a472e5(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8874dd683b7c9683dd7f774ad652d09433d7cb63a3b8558ca0fb42daf8c0f455(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd124fcf03bcbf19f064831ea2b76dbc80a38770e2e3e1991975fa3bc36f7c28(
    value: typing.Optional[DataAwsCeTagsFilterAndTags],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5bdce937e903123f3676b98d35e984765211ad37e01e9e0f2c2273a054ae756e(
    *,
    key: typing.Optional[builtins.str] = None,
    match_options: typing.Optional[typing.Sequence[builtins.str]] = None,
    values: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1f2dd646cf24472e7e8714de0aeea3663650ef8dfccf2e4b13990ebfe89b7094(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb7d22c9ee4318f06e051b8d1360828f3a20bb9edf914f659fc34f1bfc7725a9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0f970adabcce83501ae5d47d58e29d6395ff7e9d8aca4411ed2d0c7ac03642ac(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__407f927a57a93cb1d862e9122908c667c1d77fb4e936c5c12dd63fdfa95ee167(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__09ed9778b32d0bcdac6bee10515b4cb96e2594dc54477dc8fa2a2a7ba39e6e10(
    value: typing.Optional[DataAwsCeTagsFilterCostCategory],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__09ac5f3bf205a8d1187600ac7271094ba501bd725964011e518668506ac2bd40(
    *,
    key: typing.Optional[builtins.str] = None,
    match_options: typing.Optional[typing.Sequence[builtins.str]] = None,
    values: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c0ed891f755423fef9565757092530a16a9efc6128c922378a2947390848f3b6(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5a52a5e50091a55d0e5cd20e410e4a9fb8a65e4f5f4cd2ea8cfe11a847167fe1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6dfa3c9d914fec0ea33d07ab62b50a62da6f5107ddd8e4185b7f50669bc1aa6a(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c0eea3edd203ee1f00e349a11db2137ae0f05571390d029747889d88719dfbde(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6115cda1bc62db1d5cdc6cfae6248210f3af2291c7bff5bc296c19ff22f7947f(
    value: typing.Optional[DataAwsCeTagsFilterDimension],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a3854fe449096d200ab76ba47aa1e940d42537c412e2872187b7f1fd2f5aa210(
    *,
    cost_category: typing.Optional[typing.Union[DataAwsCeTagsFilterNotCostCategory, typing.Dict[builtins.str, typing.Any]]] = None,
    dimension: typing.Optional[typing.Union[DataAwsCeTagsFilterNotDimension, typing.Dict[builtins.str, typing.Any]]] = None,
    tags: typing.Optional[typing.Union[DataAwsCeTagsFilterNotTags, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a6c54ffd43706056ca39b285917e4d1a59dd76fb00516dab3f82826326d48bb7(
    *,
    key: typing.Optional[builtins.str] = None,
    match_options: typing.Optional[typing.Sequence[builtins.str]] = None,
    values: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fe9f4a111017765d368bc6ca303c8f18125fb12bc920900c60e9d270588d6192(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7dd949ea61cf85b13c7f5d237231d4e7bbefc982ccf745746f51f725940a9a50(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8acc2dc6a45fbc7077538f81f5b76e5291bc7a552fe2a2fd19508af6ab0f93ca(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__374b03371c9e16cd8fed0f61fe051b4f4d64c61d082e556decc6a45df1fe6613(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__825a6188fca608814ec406fecd2754a0527614b4efbcc25cc65b7cab5669347c(
    value: typing.Optional[DataAwsCeTagsFilterNotCostCategory],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2609ce5ff59c39e6302eb8882aa3e1c48559b4a3acc2d8b6854fc00cc10aa34a(
    *,
    key: typing.Optional[builtins.str] = None,
    match_options: typing.Optional[typing.Sequence[builtins.str]] = None,
    values: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4fd601d9d6e5608829cd6b83f44cef3c10be280d65bbccbc0b083e7294050cfb(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e5e36f8b0ab0f17b153360ca4a7eec73bf83dcf95034f642464a33e72b47d367(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__42e4ebccc6245a05045b64f59568d3eed7e4a2786cf58f32821cd39b75865651(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b8260bd87b637e665cc1e6addf152e7a5bc8bf6af8181d7cd71178a523e54408(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__75f015dcfe90ca5e605f3a99fa68b426c0d7d8391672f9e03db1a619391180ef(
    value: typing.Optional[DataAwsCeTagsFilterNotDimension],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__552861e52930ccf110f7b39ac3e0640231885481e5c697efba85724a07419321(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d750345dfbb70438e19e682dd21c8037f7631e22f02b2c459a4e6c5ec275d030(
    value: typing.Optional[DataAwsCeTagsFilterNot],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c99225f7114a5fead86920a140da0ffbfdf3c0a25e0ddfc0dc6f6818d0176b37(
    *,
    key: typing.Optional[builtins.str] = None,
    match_options: typing.Optional[typing.Sequence[builtins.str]] = None,
    values: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b951f3b8c7b0115992210e2e643c7e994c2e54d025849955cf211e81992e5136(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5f98461df53731d4b9a9c6a2e12276697066f77acad2d1b5553598978d0abbac(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ae56bcf86af8011773686d87369fc6ac556c7039257114918e1400c1c9663487(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__900d89861b773a8f6abf6f76412e8dcbe93f978b8d5b4a89a03ac77607caee6a(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c71d23634056c168cc30d2a0e66547e8234217de6686b35a02735e62b7124a7a(
    value: typing.Optional[DataAwsCeTagsFilterNotTags],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__27252865abef982091f8b7d4fc15a3a257d6a73549d9542411a6293214295074(
    *,
    cost_category: typing.Optional[typing.Union[DataAwsCeTagsFilterOrCostCategory, typing.Dict[builtins.str, typing.Any]]] = None,
    dimension: typing.Optional[typing.Union[DataAwsCeTagsFilterOrDimension, typing.Dict[builtins.str, typing.Any]]] = None,
    tags: typing.Optional[typing.Union[DataAwsCeTagsFilterOrTags, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__12216440d97711004a1221cdce9f48f6f8e8d718688676125974c8967ae66369(
    *,
    key: typing.Optional[builtins.str] = None,
    match_options: typing.Optional[typing.Sequence[builtins.str]] = None,
    values: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c51a583e181ac243cea7fb1a263b9a3f5f2d0c1298e7bb89ac8a0dde5d78df62(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__07535dbddd52354d4fb2333335d9318f92e412a0bc5e62480e7829684fa821eb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a6ff90a0671557b9d4e32468bd930f7d0b0faa44752e697fa2f7b11cc48d1b23(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__67bae31e4c9fad0c9ac7a101aa780e9e61afdd0dd99cbf9430658b5c0f2a76b4(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c24085d06711f980971d9c4e019c298474cfcf27f0de0c426a1962ece95df34d(
    value: typing.Optional[DataAwsCeTagsFilterOrCostCategory],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__92e37952e24f153dbec45b84c800177a5aa1757330fcece936e327d98ec8c59e(
    *,
    key: typing.Optional[builtins.str] = None,
    match_options: typing.Optional[typing.Sequence[builtins.str]] = None,
    values: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__45c076b8986c3ff47e02a1dd714c04bc5ff19f1cfae5c58984d4eab8f5ec5593(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__910c7f9cb815a8b1bf62e3e547a9f71852813842397e0d587c7be837641334e4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d64a573cedad135f78bd350fac9b4535f2435256096db50f23017875e26b4b7c(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__74862576fbd0471e085e84e321ccb6b71136f6f30dac90936bf638180f70507e(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ca885e8a88c9c984863512eed341f6c8583740d87146633974f6eea3eaa5367e(
    value: typing.Optional[DataAwsCeTagsFilterOrDimension],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__04abb6c36b096675d445df43c1ac58cff5e6b6a81039ec8c36dd2022a1e3d481(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5551997114c8ff12803daf63f56ca3dd5652ebb91953e466323aeb1408c2213c(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__837e3c7becd0179020d65ee3d1177665c8b05e005778fa78b7d83bff71cc0457(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__789e0d6a2b27e14f91cd417aafbbf42fb49593cdcb2ec8dae39473c6891caf28(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b8945663877ce56f506b324eed538f133b1d88b1fc2c9ce9edbc3fb9a4d097fc(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__36a0ab99707d7f22f0b15c67cc927dab26f7de2d12f49b0ff0a97b3e51244af0(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAwsCeTagsFilterOr]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dddaa11b8804c6ff6803fb4a421ad311455e955ab68024786f084e9d3c44465b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dbcd46614d8c3bfcbcc93210ce0b7e3c0e743181266e4872ac6d8344616343d5(
    value: typing.Optional[typing.Union[DataAwsCeTagsFilterOr, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7c294b64f83dfa356caed3a9bfd84aa5d69c315ebca158449f21459412ccd7f7(
    *,
    key: typing.Optional[builtins.str] = None,
    match_options: typing.Optional[typing.Sequence[builtins.str]] = None,
    values: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2110a0264b444f4e8c0acf256dbdb168418071dae219b6bdef63d514f431a432(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7ecff8fff001c6957edeb227116b80db953e65c1111bddbc5e539feb5f79884d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e7cfef665e1cdd67781c5441e4c716e2f3efdbb22e1ba1fbbd39f41815ebb5f8(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__220ac06b8b5bebf8890dfae308b18848003fb38a2585b75886b6cb570037b8f1(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__974251e0ce76d3d24ee205211fb1ef559af3f787c1a37f0ccdc40b5fb69ba4ca(
    value: typing.Optional[DataAwsCeTagsFilterOrTags],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d1c7648d5383eb93a557f420fdc9528c6e342f028f2d4dd2d485c7b2752d84d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3060121ba8c3ffc8fe9501119d254e3d96833ffece02820c49db0662819c5448(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAwsCeTagsFilterAnd, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3f06c94420f8fd43649f05b119f3913d11235527d7a6687a5b5c44e8bf8801d2(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAwsCeTagsFilterOr, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__128e349319d22f10cbb1c89eba80f01266dc6e5fba8984bc93eb0792146d05ee(
    value: typing.Optional[DataAwsCeTagsFilter],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1b2f496a1887d944a84bcf4a6ce5681421a7cb036687e766579c9b7ecf2abc15(
    *,
    key: typing.Optional[builtins.str] = None,
    match_options: typing.Optional[typing.Sequence[builtins.str]] = None,
    values: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__545b000e3ab88733ac6cf2bbf49c67afa5e322b776f8d4229eb5d002e679e633(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f49bcb12c642e3d71166a124e36f9fa70a3d977dc8d1cbeb13be036f801ed840(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dc2efbff5d8de9b853153a78e4f9c38a9d0ce6c0b7c556499e7591c34c90dc33(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0357c65985f90fee9805318977664797228bd8f02eb77cb3186df1c1942fc27c(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5b731ae38bfde0db9842c3393cdd9de680a8f7c74a431e0273db6b74e9550b11(
    value: typing.Optional[DataAwsCeTagsFilterTags],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b8838cad26be5f6fa548b3944779c03f40b6ee18fa475ffe832d7328e52e6a1d(
    *,
    key: typing.Optional[builtins.str] = None,
    sort_order: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__005cedf17f793a9d3a4378eb67709255f35fec44cf70555867a92f7c6d8100b7(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__42f2728b1db7f055cae0976a213f34f3e32c152b49f6a568fbaf6b798f0a2a01(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__abc35fa9db450bf53af55a56d60315b0929e423c8b1f64e3ef4393f6c0f0bb81(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a681fb260dcf67a1a39559cecca628b6845edfa0f5d18b6e9ca27d974bd7dec3(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c4efb7625b0136daf6c07bc153c36d414557cd55355a39157a5fb45de00b7323(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f562cf51f28137c28c229673674cd4e6b1df17f3a6773f9155d071edd20c43db(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAwsCeTagsSortBy]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a4c6a48e2b3d4367bbd11035490942ceab1d4ce358efb46f686774d88027325f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a42b040ba0ffb6298324b8ba9c5c42e178a1650967edd9a5e7d59d4e5607168a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__11270a2a74e001c64c9a1617528d9b60319a1906a0210dd052b71358b7601aa3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9ecf585a63b7d3d44b22c2b859db4196a6f16482bcaf00fe16fc5c5936848f4b(
    value: typing.Optional[typing.Union[DataAwsCeTagsSortBy, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f74b314690e24282b2b25a8a0893cc196570e383bf04ab46fe33e99f64dde31e(
    *,
    end: builtins.str,
    start: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__915cf174913eb9adf2f09ef60651ea441efb42a42f2dc059e2fbe03b714fdd23(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__705c33fb0a1f05c9715595643aac5ea518178ac5d696ad2917a471d832431379(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ff069614b257386a6be9413cca9ab574a4317573a155434e40a7b84684314c66(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c217d373607c3f5defdcaa5a3238ae8096d44de5a1a89dfc72b58844d1ee137c(
    value: typing.Optional[DataAwsCeTagsTimePeriod],
) -> None:
    """Type checking stubs"""
    pass
