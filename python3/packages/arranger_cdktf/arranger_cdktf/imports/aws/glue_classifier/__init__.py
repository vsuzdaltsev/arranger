'''
# `aws_glue_classifier`

Refer to the Terraform Registory for docs: [`aws_glue_classifier`](https://www.terraform.io/docs/providers/aws/r/glue_classifier).
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


class GlueClassifier(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.glueClassifier.GlueClassifier",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/glue_classifier aws_glue_classifier}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        csv_classifier: typing.Optional[typing.Union["GlueClassifierCsvClassifier", typing.Dict[builtins.str, typing.Any]]] = None,
        grok_classifier: typing.Optional[typing.Union["GlueClassifierGrokClassifier", typing.Dict[builtins.str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        json_classifier: typing.Optional[typing.Union["GlueClassifierJsonClassifier", typing.Dict[builtins.str, typing.Any]]] = None,
        xml_classifier: typing.Optional[typing.Union["GlueClassifierXmlClassifier", typing.Dict[builtins.str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/glue_classifier aws_glue_classifier} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_classifier#name GlueClassifier#name}.
        :param csv_classifier: csv_classifier block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_classifier#csv_classifier GlueClassifier#csv_classifier}
        :param grok_classifier: grok_classifier block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_classifier#grok_classifier GlueClassifier#grok_classifier}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_classifier#id GlueClassifier#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param json_classifier: json_classifier block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_classifier#json_classifier GlueClassifier#json_classifier}
        :param xml_classifier: xml_classifier block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_classifier#xml_classifier GlueClassifier#xml_classifier}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e2236f8cf294e74bf8c2dc001947a9a7dfa1aae1564c3f9acdf21c68d980fec1)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = GlueClassifierConfig(
            name=name,
            csv_classifier=csv_classifier,
            grok_classifier=grok_classifier,
            id=id,
            json_classifier=json_classifier,
            xml_classifier=xml_classifier,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putCsvClassifier")
    def put_csv_classifier(
        self,
        *,
        allow_single_column: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        contains_header: typing.Optional[builtins.str] = None,
        custom_datatype_configured: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        custom_datatypes: typing.Optional[typing.Sequence[builtins.str]] = None,
        delimiter: typing.Optional[builtins.str] = None,
        disable_value_trimming: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        header: typing.Optional[typing.Sequence[builtins.str]] = None,
        quote_symbol: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param allow_single_column: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_classifier#allow_single_column GlueClassifier#allow_single_column}.
        :param contains_header: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_classifier#contains_header GlueClassifier#contains_header}.
        :param custom_datatype_configured: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_classifier#custom_datatype_configured GlueClassifier#custom_datatype_configured}.
        :param custom_datatypes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_classifier#custom_datatypes GlueClassifier#custom_datatypes}.
        :param delimiter: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_classifier#delimiter GlueClassifier#delimiter}.
        :param disable_value_trimming: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_classifier#disable_value_trimming GlueClassifier#disable_value_trimming}.
        :param header: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_classifier#header GlueClassifier#header}.
        :param quote_symbol: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_classifier#quote_symbol GlueClassifier#quote_symbol}.
        '''
        value = GlueClassifierCsvClassifier(
            allow_single_column=allow_single_column,
            contains_header=contains_header,
            custom_datatype_configured=custom_datatype_configured,
            custom_datatypes=custom_datatypes,
            delimiter=delimiter,
            disable_value_trimming=disable_value_trimming,
            header=header,
            quote_symbol=quote_symbol,
        )

        return typing.cast(None, jsii.invoke(self, "putCsvClassifier", [value]))

    @jsii.member(jsii_name="putGrokClassifier")
    def put_grok_classifier(
        self,
        *,
        classification: builtins.str,
        grok_pattern: builtins.str,
        custom_patterns: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param classification: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_classifier#classification GlueClassifier#classification}.
        :param grok_pattern: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_classifier#grok_pattern GlueClassifier#grok_pattern}.
        :param custom_patterns: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_classifier#custom_patterns GlueClassifier#custom_patterns}.
        '''
        value = GlueClassifierGrokClassifier(
            classification=classification,
            grok_pattern=grok_pattern,
            custom_patterns=custom_patterns,
        )

        return typing.cast(None, jsii.invoke(self, "putGrokClassifier", [value]))

    @jsii.member(jsii_name="putJsonClassifier")
    def put_json_classifier(self, *, json_path: builtins.str) -> None:
        '''
        :param json_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_classifier#json_path GlueClassifier#json_path}.
        '''
        value = GlueClassifierJsonClassifier(json_path=json_path)

        return typing.cast(None, jsii.invoke(self, "putJsonClassifier", [value]))

    @jsii.member(jsii_name="putXmlClassifier")
    def put_xml_classifier(
        self,
        *,
        classification: builtins.str,
        row_tag: builtins.str,
    ) -> None:
        '''
        :param classification: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_classifier#classification GlueClassifier#classification}.
        :param row_tag: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_classifier#row_tag GlueClassifier#row_tag}.
        '''
        value = GlueClassifierXmlClassifier(
            classification=classification, row_tag=row_tag
        )

        return typing.cast(None, jsii.invoke(self, "putXmlClassifier", [value]))

    @jsii.member(jsii_name="resetCsvClassifier")
    def reset_csv_classifier(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCsvClassifier", []))

    @jsii.member(jsii_name="resetGrokClassifier")
    def reset_grok_classifier(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGrokClassifier", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetJsonClassifier")
    def reset_json_classifier(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetJsonClassifier", []))

    @jsii.member(jsii_name="resetXmlClassifier")
    def reset_xml_classifier(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetXmlClassifier", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="csvClassifier")
    def csv_classifier(self) -> "GlueClassifierCsvClassifierOutputReference":
        return typing.cast("GlueClassifierCsvClassifierOutputReference", jsii.get(self, "csvClassifier"))

    @builtins.property
    @jsii.member(jsii_name="grokClassifier")
    def grok_classifier(self) -> "GlueClassifierGrokClassifierOutputReference":
        return typing.cast("GlueClassifierGrokClassifierOutputReference", jsii.get(self, "grokClassifier"))

    @builtins.property
    @jsii.member(jsii_name="jsonClassifier")
    def json_classifier(self) -> "GlueClassifierJsonClassifierOutputReference":
        return typing.cast("GlueClassifierJsonClassifierOutputReference", jsii.get(self, "jsonClassifier"))

    @builtins.property
    @jsii.member(jsii_name="xmlClassifier")
    def xml_classifier(self) -> "GlueClassifierXmlClassifierOutputReference":
        return typing.cast("GlueClassifierXmlClassifierOutputReference", jsii.get(self, "xmlClassifier"))

    @builtins.property
    @jsii.member(jsii_name="csvClassifierInput")
    def csv_classifier_input(self) -> typing.Optional["GlueClassifierCsvClassifier"]:
        return typing.cast(typing.Optional["GlueClassifierCsvClassifier"], jsii.get(self, "csvClassifierInput"))

    @builtins.property
    @jsii.member(jsii_name="grokClassifierInput")
    def grok_classifier_input(self) -> typing.Optional["GlueClassifierGrokClassifier"]:
        return typing.cast(typing.Optional["GlueClassifierGrokClassifier"], jsii.get(self, "grokClassifierInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="jsonClassifierInput")
    def json_classifier_input(self) -> typing.Optional["GlueClassifierJsonClassifier"]:
        return typing.cast(typing.Optional["GlueClassifierJsonClassifier"], jsii.get(self, "jsonClassifierInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="xmlClassifierInput")
    def xml_classifier_input(self) -> typing.Optional["GlueClassifierXmlClassifier"]:
        return typing.cast(typing.Optional["GlueClassifierXmlClassifier"], jsii.get(self, "xmlClassifierInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7337c6dce43d0dfe136322e30f0084f3a91c6c78b2450ea464f2a10c2fc4fef8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__217febef073103b71dac6bbe0969e5ddefb723328fb4d2301f528cf08ccfcc3b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)


@jsii.data_type(
    jsii_type="aws.glueClassifier.GlueClassifierConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "name": "name",
        "csv_classifier": "csvClassifier",
        "grok_classifier": "grokClassifier",
        "id": "id",
        "json_classifier": "jsonClassifier",
        "xml_classifier": "xmlClassifier",
    },
)
class GlueClassifierConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        name: builtins.str,
        csv_classifier: typing.Optional[typing.Union["GlueClassifierCsvClassifier", typing.Dict[builtins.str, typing.Any]]] = None,
        grok_classifier: typing.Optional[typing.Union["GlueClassifierGrokClassifier", typing.Dict[builtins.str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        json_classifier: typing.Optional[typing.Union["GlueClassifierJsonClassifier", typing.Dict[builtins.str, typing.Any]]] = None,
        xml_classifier: typing.Optional[typing.Union["GlueClassifierXmlClassifier", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_classifier#name GlueClassifier#name}.
        :param csv_classifier: csv_classifier block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_classifier#csv_classifier GlueClassifier#csv_classifier}
        :param grok_classifier: grok_classifier block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_classifier#grok_classifier GlueClassifier#grok_classifier}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_classifier#id GlueClassifier#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param json_classifier: json_classifier block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_classifier#json_classifier GlueClassifier#json_classifier}
        :param xml_classifier: xml_classifier block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_classifier#xml_classifier GlueClassifier#xml_classifier}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(csv_classifier, dict):
            csv_classifier = GlueClassifierCsvClassifier(**csv_classifier)
        if isinstance(grok_classifier, dict):
            grok_classifier = GlueClassifierGrokClassifier(**grok_classifier)
        if isinstance(json_classifier, dict):
            json_classifier = GlueClassifierJsonClassifier(**json_classifier)
        if isinstance(xml_classifier, dict):
            xml_classifier = GlueClassifierXmlClassifier(**xml_classifier)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__11188ec49ce2e7a8d00ecf5a4b0f640297c68401735490d005d761499a59eafc)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument csv_classifier", value=csv_classifier, expected_type=type_hints["csv_classifier"])
            check_type(argname="argument grok_classifier", value=grok_classifier, expected_type=type_hints["grok_classifier"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument json_classifier", value=json_classifier, expected_type=type_hints["json_classifier"])
            check_type(argname="argument xml_classifier", value=xml_classifier, expected_type=type_hints["xml_classifier"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
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
        if csv_classifier is not None:
            self._values["csv_classifier"] = csv_classifier
        if grok_classifier is not None:
            self._values["grok_classifier"] = grok_classifier
        if id is not None:
            self._values["id"] = id
        if json_classifier is not None:
            self._values["json_classifier"] = json_classifier
        if xml_classifier is not None:
            self._values["xml_classifier"] = xml_classifier

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
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_classifier#name GlueClassifier#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def csv_classifier(self) -> typing.Optional["GlueClassifierCsvClassifier"]:
        '''csv_classifier block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_classifier#csv_classifier GlueClassifier#csv_classifier}
        '''
        result = self._values.get("csv_classifier")
        return typing.cast(typing.Optional["GlueClassifierCsvClassifier"], result)

    @builtins.property
    def grok_classifier(self) -> typing.Optional["GlueClassifierGrokClassifier"]:
        '''grok_classifier block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_classifier#grok_classifier GlueClassifier#grok_classifier}
        '''
        result = self._values.get("grok_classifier")
        return typing.cast(typing.Optional["GlueClassifierGrokClassifier"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_classifier#id GlueClassifier#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def json_classifier(self) -> typing.Optional["GlueClassifierJsonClassifier"]:
        '''json_classifier block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_classifier#json_classifier GlueClassifier#json_classifier}
        '''
        result = self._values.get("json_classifier")
        return typing.cast(typing.Optional["GlueClassifierJsonClassifier"], result)

    @builtins.property
    def xml_classifier(self) -> typing.Optional["GlueClassifierXmlClassifier"]:
        '''xml_classifier block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_classifier#xml_classifier GlueClassifier#xml_classifier}
        '''
        result = self._values.get("xml_classifier")
        return typing.cast(typing.Optional["GlueClassifierXmlClassifier"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GlueClassifierConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.glueClassifier.GlueClassifierCsvClassifier",
    jsii_struct_bases=[],
    name_mapping={
        "allow_single_column": "allowSingleColumn",
        "contains_header": "containsHeader",
        "custom_datatype_configured": "customDatatypeConfigured",
        "custom_datatypes": "customDatatypes",
        "delimiter": "delimiter",
        "disable_value_trimming": "disableValueTrimming",
        "header": "header",
        "quote_symbol": "quoteSymbol",
    },
)
class GlueClassifierCsvClassifier:
    def __init__(
        self,
        *,
        allow_single_column: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        contains_header: typing.Optional[builtins.str] = None,
        custom_datatype_configured: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        custom_datatypes: typing.Optional[typing.Sequence[builtins.str]] = None,
        delimiter: typing.Optional[builtins.str] = None,
        disable_value_trimming: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        header: typing.Optional[typing.Sequence[builtins.str]] = None,
        quote_symbol: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param allow_single_column: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_classifier#allow_single_column GlueClassifier#allow_single_column}.
        :param contains_header: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_classifier#contains_header GlueClassifier#contains_header}.
        :param custom_datatype_configured: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_classifier#custom_datatype_configured GlueClassifier#custom_datatype_configured}.
        :param custom_datatypes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_classifier#custom_datatypes GlueClassifier#custom_datatypes}.
        :param delimiter: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_classifier#delimiter GlueClassifier#delimiter}.
        :param disable_value_trimming: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_classifier#disable_value_trimming GlueClassifier#disable_value_trimming}.
        :param header: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_classifier#header GlueClassifier#header}.
        :param quote_symbol: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_classifier#quote_symbol GlueClassifier#quote_symbol}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a93fcbb922f05df0623a278c4440ab064e06180db848b864d68007232c68e8ca)
            check_type(argname="argument allow_single_column", value=allow_single_column, expected_type=type_hints["allow_single_column"])
            check_type(argname="argument contains_header", value=contains_header, expected_type=type_hints["contains_header"])
            check_type(argname="argument custom_datatype_configured", value=custom_datatype_configured, expected_type=type_hints["custom_datatype_configured"])
            check_type(argname="argument custom_datatypes", value=custom_datatypes, expected_type=type_hints["custom_datatypes"])
            check_type(argname="argument delimiter", value=delimiter, expected_type=type_hints["delimiter"])
            check_type(argname="argument disable_value_trimming", value=disable_value_trimming, expected_type=type_hints["disable_value_trimming"])
            check_type(argname="argument header", value=header, expected_type=type_hints["header"])
            check_type(argname="argument quote_symbol", value=quote_symbol, expected_type=type_hints["quote_symbol"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if allow_single_column is not None:
            self._values["allow_single_column"] = allow_single_column
        if contains_header is not None:
            self._values["contains_header"] = contains_header
        if custom_datatype_configured is not None:
            self._values["custom_datatype_configured"] = custom_datatype_configured
        if custom_datatypes is not None:
            self._values["custom_datatypes"] = custom_datatypes
        if delimiter is not None:
            self._values["delimiter"] = delimiter
        if disable_value_trimming is not None:
            self._values["disable_value_trimming"] = disable_value_trimming
        if header is not None:
            self._values["header"] = header
        if quote_symbol is not None:
            self._values["quote_symbol"] = quote_symbol

    @builtins.property
    def allow_single_column(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_classifier#allow_single_column GlueClassifier#allow_single_column}.'''
        result = self._values.get("allow_single_column")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def contains_header(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_classifier#contains_header GlueClassifier#contains_header}.'''
        result = self._values.get("contains_header")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def custom_datatype_configured(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_classifier#custom_datatype_configured GlueClassifier#custom_datatype_configured}.'''
        result = self._values.get("custom_datatype_configured")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def custom_datatypes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_classifier#custom_datatypes GlueClassifier#custom_datatypes}.'''
        result = self._values.get("custom_datatypes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def delimiter(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_classifier#delimiter GlueClassifier#delimiter}.'''
        result = self._values.get("delimiter")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def disable_value_trimming(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_classifier#disable_value_trimming GlueClassifier#disable_value_trimming}.'''
        result = self._values.get("disable_value_trimming")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def header(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_classifier#header GlueClassifier#header}.'''
        result = self._values.get("header")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def quote_symbol(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_classifier#quote_symbol GlueClassifier#quote_symbol}.'''
        result = self._values.get("quote_symbol")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GlueClassifierCsvClassifier(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GlueClassifierCsvClassifierOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.glueClassifier.GlueClassifierCsvClassifierOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__2dec6caebed71bf35a1b78e6f4d77a39c7691c9eae4668b2d5e715f5ecd71afe)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAllowSingleColumn")
    def reset_allow_single_column(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowSingleColumn", []))

    @jsii.member(jsii_name="resetContainsHeader")
    def reset_contains_header(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContainsHeader", []))

    @jsii.member(jsii_name="resetCustomDatatypeConfigured")
    def reset_custom_datatype_configured(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomDatatypeConfigured", []))

    @jsii.member(jsii_name="resetCustomDatatypes")
    def reset_custom_datatypes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomDatatypes", []))

    @jsii.member(jsii_name="resetDelimiter")
    def reset_delimiter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDelimiter", []))

    @jsii.member(jsii_name="resetDisableValueTrimming")
    def reset_disable_value_trimming(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisableValueTrimming", []))

    @jsii.member(jsii_name="resetHeader")
    def reset_header(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHeader", []))

    @jsii.member(jsii_name="resetQuoteSymbol")
    def reset_quote_symbol(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetQuoteSymbol", []))

    @builtins.property
    @jsii.member(jsii_name="allowSingleColumnInput")
    def allow_single_column_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "allowSingleColumnInput"))

    @builtins.property
    @jsii.member(jsii_name="containsHeaderInput")
    def contains_header_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "containsHeaderInput"))

    @builtins.property
    @jsii.member(jsii_name="customDatatypeConfiguredInput")
    def custom_datatype_configured_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "customDatatypeConfiguredInput"))

    @builtins.property
    @jsii.member(jsii_name="customDatatypesInput")
    def custom_datatypes_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "customDatatypesInput"))

    @builtins.property
    @jsii.member(jsii_name="delimiterInput")
    def delimiter_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "delimiterInput"))

    @builtins.property
    @jsii.member(jsii_name="disableValueTrimmingInput")
    def disable_value_trimming_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "disableValueTrimmingInput"))

    @builtins.property
    @jsii.member(jsii_name="headerInput")
    def header_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "headerInput"))

    @builtins.property
    @jsii.member(jsii_name="quoteSymbolInput")
    def quote_symbol_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "quoteSymbolInput"))

    @builtins.property
    @jsii.member(jsii_name="allowSingleColumn")
    def allow_single_column(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "allowSingleColumn"))

    @allow_single_column.setter
    def allow_single_column(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fc6d14fc41af9d797ea9ccd6bd61a9e4b7f258f6502998512bfc2429f7c3b24e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowSingleColumn", value)

    @builtins.property
    @jsii.member(jsii_name="containsHeader")
    def contains_header(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "containsHeader"))

    @contains_header.setter
    def contains_header(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c97b1ecfdd47838cb35d9e3b03e523f5b0c815a8927a12215aaa24ed66973ddc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "containsHeader", value)

    @builtins.property
    @jsii.member(jsii_name="customDatatypeConfigured")
    def custom_datatype_configured(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "customDatatypeConfigured"))

    @custom_datatype_configured.setter
    def custom_datatype_configured(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f970cc100fcf9a4171d5d9451604b1426f1e00d5d6d12945cf2f88378735bbc4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customDatatypeConfigured", value)

    @builtins.property
    @jsii.member(jsii_name="customDatatypes")
    def custom_datatypes(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "customDatatypes"))

    @custom_datatypes.setter
    def custom_datatypes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c1be5c9df16a3dd8071e1494dfe48b7b8fbc98e2096d4deda961defa774285a5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customDatatypes", value)

    @builtins.property
    @jsii.member(jsii_name="delimiter")
    def delimiter(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delimiter"))

    @delimiter.setter
    def delimiter(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6121d4eb68a3a44f448bac17fc1ccd0e4013fb448e34655b844b504d2c5e2f54)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delimiter", value)

    @builtins.property
    @jsii.member(jsii_name="disableValueTrimming")
    def disable_value_trimming(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "disableValueTrimming"))

    @disable_value_trimming.setter
    def disable_value_trimming(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9085dc84a3db6a8a947629f271b3214bd4b83e883dc26c6de3753a52959fd745)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disableValueTrimming", value)

    @builtins.property
    @jsii.member(jsii_name="header")
    def header(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "header"))

    @header.setter
    def header(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f98bc1f3230745ccca2f74ed06fce9c713fb3841f22cf2ad867eb670c31a65f6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "header", value)

    @builtins.property
    @jsii.member(jsii_name="quoteSymbol")
    def quote_symbol(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "quoteSymbol"))

    @quote_symbol.setter
    def quote_symbol(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__943e452650207f128e4274ee83e3297b92799e0eee16da321fd2a7cb1115e8a4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "quoteSymbol", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GlueClassifierCsvClassifier]:
        return typing.cast(typing.Optional[GlueClassifierCsvClassifier], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GlueClassifierCsvClassifier],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8a8bf1501e9a2df11f634f45adaa02c2c9dd286a9ef6576179e8162612f152bf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.glueClassifier.GlueClassifierGrokClassifier",
    jsii_struct_bases=[],
    name_mapping={
        "classification": "classification",
        "grok_pattern": "grokPattern",
        "custom_patterns": "customPatterns",
    },
)
class GlueClassifierGrokClassifier:
    def __init__(
        self,
        *,
        classification: builtins.str,
        grok_pattern: builtins.str,
        custom_patterns: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param classification: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_classifier#classification GlueClassifier#classification}.
        :param grok_pattern: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_classifier#grok_pattern GlueClassifier#grok_pattern}.
        :param custom_patterns: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_classifier#custom_patterns GlueClassifier#custom_patterns}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__07510dac0a31c81f950a2f39f5df54b9d80e6deb7f23c73e68507219a9dcd390)
            check_type(argname="argument classification", value=classification, expected_type=type_hints["classification"])
            check_type(argname="argument grok_pattern", value=grok_pattern, expected_type=type_hints["grok_pattern"])
            check_type(argname="argument custom_patterns", value=custom_patterns, expected_type=type_hints["custom_patterns"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "classification": classification,
            "grok_pattern": grok_pattern,
        }
        if custom_patterns is not None:
            self._values["custom_patterns"] = custom_patterns

    @builtins.property
    def classification(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_classifier#classification GlueClassifier#classification}.'''
        result = self._values.get("classification")
        assert result is not None, "Required property 'classification' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def grok_pattern(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_classifier#grok_pattern GlueClassifier#grok_pattern}.'''
        result = self._values.get("grok_pattern")
        assert result is not None, "Required property 'grok_pattern' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def custom_patterns(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_classifier#custom_patterns GlueClassifier#custom_patterns}.'''
        result = self._values.get("custom_patterns")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GlueClassifierGrokClassifier(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GlueClassifierGrokClassifierOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.glueClassifier.GlueClassifierGrokClassifierOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f953786c52d2a334ab9f641995eed045a4efeaaffb7e8465e9bb655dee6b7d57)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCustomPatterns")
    def reset_custom_patterns(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomPatterns", []))

    @builtins.property
    @jsii.member(jsii_name="classificationInput")
    def classification_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "classificationInput"))

    @builtins.property
    @jsii.member(jsii_name="customPatternsInput")
    def custom_patterns_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "customPatternsInput"))

    @builtins.property
    @jsii.member(jsii_name="grokPatternInput")
    def grok_pattern_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "grokPatternInput"))

    @builtins.property
    @jsii.member(jsii_name="classification")
    def classification(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "classification"))

    @classification.setter
    def classification(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dccd38a5c2b29b185cdddcc97c489b508b768d34855f444d6375ffc0115b1c5b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "classification", value)

    @builtins.property
    @jsii.member(jsii_name="customPatterns")
    def custom_patterns(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "customPatterns"))

    @custom_patterns.setter
    def custom_patterns(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__99241f26422066d6d640ff0c50704662bea375ea41a62c36f569c3d30b815789)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customPatterns", value)

    @builtins.property
    @jsii.member(jsii_name="grokPattern")
    def grok_pattern(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "grokPattern"))

    @grok_pattern.setter
    def grok_pattern(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d83a82bf7fa0a38657a52b498efca6c9449424b6346a6a43284ae36a3213b67b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "grokPattern", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GlueClassifierGrokClassifier]:
        return typing.cast(typing.Optional[GlueClassifierGrokClassifier], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GlueClassifierGrokClassifier],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f0d7093f4e9283341220a39d53ff71a30b62a7d2d0ad4517f274645b4a525785)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.glueClassifier.GlueClassifierJsonClassifier",
    jsii_struct_bases=[],
    name_mapping={"json_path": "jsonPath"},
)
class GlueClassifierJsonClassifier:
    def __init__(self, *, json_path: builtins.str) -> None:
        '''
        :param json_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_classifier#json_path GlueClassifier#json_path}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d4d07eb0767e18cf21d88f1f681cc8a7e5a3de698574ee1fa918ce17dcac7786)
            check_type(argname="argument json_path", value=json_path, expected_type=type_hints["json_path"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "json_path": json_path,
        }

    @builtins.property
    def json_path(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_classifier#json_path GlueClassifier#json_path}.'''
        result = self._values.get("json_path")
        assert result is not None, "Required property 'json_path' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GlueClassifierJsonClassifier(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GlueClassifierJsonClassifierOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.glueClassifier.GlueClassifierJsonClassifierOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__73c7a46f7f7110b1a1c9b3eb6b2540a17249794e439b1e10072ad74fbdef809c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="jsonPathInput")
    def json_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "jsonPathInput"))

    @builtins.property
    @jsii.member(jsii_name="jsonPath")
    def json_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "jsonPath"))

    @json_path.setter
    def json_path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4f9022a7719af6bec224d0d52d19b8cdffa43ea090ae74951d3646ff127311b2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "jsonPath", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GlueClassifierJsonClassifier]:
        return typing.cast(typing.Optional[GlueClassifierJsonClassifier], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GlueClassifierJsonClassifier],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__16a96fb8a5554b12a0c5268d788e6c8ad06a43e756632865429cea45540ba12d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.glueClassifier.GlueClassifierXmlClassifier",
    jsii_struct_bases=[],
    name_mapping={"classification": "classification", "row_tag": "rowTag"},
)
class GlueClassifierXmlClassifier:
    def __init__(self, *, classification: builtins.str, row_tag: builtins.str) -> None:
        '''
        :param classification: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_classifier#classification GlueClassifier#classification}.
        :param row_tag: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_classifier#row_tag GlueClassifier#row_tag}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e32d3ffbeeddf6789635512936deab4bc056727c4c7d8da169bddc7ad5ff2e79)
            check_type(argname="argument classification", value=classification, expected_type=type_hints["classification"])
            check_type(argname="argument row_tag", value=row_tag, expected_type=type_hints["row_tag"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "classification": classification,
            "row_tag": row_tag,
        }

    @builtins.property
    def classification(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_classifier#classification GlueClassifier#classification}.'''
        result = self._values.get("classification")
        assert result is not None, "Required property 'classification' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def row_tag(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_classifier#row_tag GlueClassifier#row_tag}.'''
        result = self._values.get("row_tag")
        assert result is not None, "Required property 'row_tag' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GlueClassifierXmlClassifier(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GlueClassifierXmlClassifierOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.glueClassifier.GlueClassifierXmlClassifierOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__2345d280cfcb7a4c83da4f4cdc850777ea7d35f59b26589fcb97ef4c39536ca7)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="classificationInput")
    def classification_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "classificationInput"))

    @builtins.property
    @jsii.member(jsii_name="rowTagInput")
    def row_tag_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "rowTagInput"))

    @builtins.property
    @jsii.member(jsii_name="classification")
    def classification(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "classification"))

    @classification.setter
    def classification(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5a4e96349b0967a06db28009209ef516e22a2bbda4b4a692a686bba455a1ea9c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "classification", value)

    @builtins.property
    @jsii.member(jsii_name="rowTag")
    def row_tag(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "rowTag"))

    @row_tag.setter
    def row_tag(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__615a46e133f91cc10d64a6612053f645b726cfe442cf6abc8836b9d9b488e37b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rowTag", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GlueClassifierXmlClassifier]:
        return typing.cast(typing.Optional[GlueClassifierXmlClassifier], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GlueClassifierXmlClassifier],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1e22fb837f2f038d305b09927b26e666233300f5adaefd7967af95f013ff49e4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "GlueClassifier",
    "GlueClassifierConfig",
    "GlueClassifierCsvClassifier",
    "GlueClassifierCsvClassifierOutputReference",
    "GlueClassifierGrokClassifier",
    "GlueClassifierGrokClassifierOutputReference",
    "GlueClassifierJsonClassifier",
    "GlueClassifierJsonClassifierOutputReference",
    "GlueClassifierXmlClassifier",
    "GlueClassifierXmlClassifierOutputReference",
]

publication.publish()

def _typecheckingstub__e2236f8cf294e74bf8c2dc001947a9a7dfa1aae1564c3f9acdf21c68d980fec1(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    name: builtins.str,
    csv_classifier: typing.Optional[typing.Union[GlueClassifierCsvClassifier, typing.Dict[builtins.str, typing.Any]]] = None,
    grok_classifier: typing.Optional[typing.Union[GlueClassifierGrokClassifier, typing.Dict[builtins.str, typing.Any]]] = None,
    id: typing.Optional[builtins.str] = None,
    json_classifier: typing.Optional[typing.Union[GlueClassifierJsonClassifier, typing.Dict[builtins.str, typing.Any]]] = None,
    xml_classifier: typing.Optional[typing.Union[GlueClassifierXmlClassifier, typing.Dict[builtins.str, typing.Any]]] = None,
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

def _typecheckingstub__7337c6dce43d0dfe136322e30f0084f3a91c6c78b2450ea464f2a10c2fc4fef8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__217febef073103b71dac6bbe0969e5ddefb723328fb4d2301f528cf08ccfcc3b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__11188ec49ce2e7a8d00ecf5a4b0f640297c68401735490d005d761499a59eafc(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    name: builtins.str,
    csv_classifier: typing.Optional[typing.Union[GlueClassifierCsvClassifier, typing.Dict[builtins.str, typing.Any]]] = None,
    grok_classifier: typing.Optional[typing.Union[GlueClassifierGrokClassifier, typing.Dict[builtins.str, typing.Any]]] = None,
    id: typing.Optional[builtins.str] = None,
    json_classifier: typing.Optional[typing.Union[GlueClassifierJsonClassifier, typing.Dict[builtins.str, typing.Any]]] = None,
    xml_classifier: typing.Optional[typing.Union[GlueClassifierXmlClassifier, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a93fcbb922f05df0623a278c4440ab064e06180db848b864d68007232c68e8ca(
    *,
    allow_single_column: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    contains_header: typing.Optional[builtins.str] = None,
    custom_datatype_configured: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    custom_datatypes: typing.Optional[typing.Sequence[builtins.str]] = None,
    delimiter: typing.Optional[builtins.str] = None,
    disable_value_trimming: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    header: typing.Optional[typing.Sequence[builtins.str]] = None,
    quote_symbol: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2dec6caebed71bf35a1b78e6f4d77a39c7691c9eae4668b2d5e715f5ecd71afe(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc6d14fc41af9d797ea9ccd6bd61a9e4b7f258f6502998512bfc2429f7c3b24e(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c97b1ecfdd47838cb35d9e3b03e523f5b0c815a8927a12215aaa24ed66973ddc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f970cc100fcf9a4171d5d9451604b1426f1e00d5d6d12945cf2f88378735bbc4(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c1be5c9df16a3dd8071e1494dfe48b7b8fbc98e2096d4deda961defa774285a5(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6121d4eb68a3a44f448bac17fc1ccd0e4013fb448e34655b844b504d2c5e2f54(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9085dc84a3db6a8a947629f271b3214bd4b83e883dc26c6de3753a52959fd745(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f98bc1f3230745ccca2f74ed06fce9c713fb3841f22cf2ad867eb670c31a65f6(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__943e452650207f128e4274ee83e3297b92799e0eee16da321fd2a7cb1115e8a4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8a8bf1501e9a2df11f634f45adaa02c2c9dd286a9ef6576179e8162612f152bf(
    value: typing.Optional[GlueClassifierCsvClassifier],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__07510dac0a31c81f950a2f39f5df54b9d80e6deb7f23c73e68507219a9dcd390(
    *,
    classification: builtins.str,
    grok_pattern: builtins.str,
    custom_patterns: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f953786c52d2a334ab9f641995eed045a4efeaaffb7e8465e9bb655dee6b7d57(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dccd38a5c2b29b185cdddcc97c489b508b768d34855f444d6375ffc0115b1c5b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__99241f26422066d6d640ff0c50704662bea375ea41a62c36f569c3d30b815789(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d83a82bf7fa0a38657a52b498efca6c9449424b6346a6a43284ae36a3213b67b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f0d7093f4e9283341220a39d53ff71a30b62a7d2d0ad4517f274645b4a525785(
    value: typing.Optional[GlueClassifierGrokClassifier],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d4d07eb0767e18cf21d88f1f681cc8a7e5a3de698574ee1fa918ce17dcac7786(
    *,
    json_path: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__73c7a46f7f7110b1a1c9b3eb6b2540a17249794e439b1e10072ad74fbdef809c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f9022a7719af6bec224d0d52d19b8cdffa43ea090ae74951d3646ff127311b2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__16a96fb8a5554b12a0c5268d788e6c8ad06a43e756632865429cea45540ba12d(
    value: typing.Optional[GlueClassifierJsonClassifier],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e32d3ffbeeddf6789635512936deab4bc056727c4c7d8da169bddc7ad5ff2e79(
    *,
    classification: builtins.str,
    row_tag: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2345d280cfcb7a4c83da4f4cdc850777ea7d35f59b26589fcb97ef4c39536ca7(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5a4e96349b0967a06db28009209ef516e22a2bbda4b4a692a686bba455a1ea9c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__615a46e133f91cc10d64a6612053f645b726cfe442cf6abc8836b9d9b488e37b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1e22fb837f2f038d305b09927b26e666233300f5adaefd7967af95f013ff49e4(
    value: typing.Optional[GlueClassifierXmlClassifier],
) -> None:
    """Type checking stubs"""
    pass
